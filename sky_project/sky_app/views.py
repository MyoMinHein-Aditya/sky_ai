import uuid
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import ollama

from .models import ChatSession, ChatMessage


SYSTEM_PROMPT = {
    'role': 'system',
    'content': 'Your name is SKY. You are a fast, efficient AI assistant. Keep responses brief and professional. Address the user as Sir.'
}


def index(request):
    """Renders the SKY Terminal Interface"""
    return render(request, 'sky_app/index.html')


def get_or_create_session(request):
    """
    Gets the current chat session from Django's session framework.
    Creates a new one if this is a fresh browser session.
    """
    session_id = request.session.get('sky_session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['sky_session_id'] = session_id

    session, _ = ChatSession.objects.get_or_create(session_id=session_id)
    return session


class SkyChatAPI(APIView):
    """Local brain of SKY using TinyDolphin — with memory"""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        user_message = request.data.get('message', '').strip()

        if not user_message:
            return Response({"response": "System awaiting command, Sir."}, status=400)

        # Step 1: Get or create the DB session for this browser
        session = get_or_create_session(request)

        # Step 2: Save the user's message to the database
        ChatMessage.objects.create(
            session=session,
            role='user',
            content=user_message
        )

        # Step 3: Build full conversation history from the database
        # This is what gives SKY memory — every message is replayed to Ollama
        past_messages = session.messages.all()
        ollama_messages = [SYSTEM_PROMPT] + [
            {'role': msg.role, 'content': msg.content}
            for msg in past_messages
        ]

        # If a file was attached, inject its content into the last user message
        file_name = request.data.get('file_name', '').strip()
        file_content = request.data.get('file_content', '').strip()
        if file_name and file_content:
            # Truncate to ~12000 chars to stay within TinyDolphin context window
            truncated = file_content[:12000]
            was_truncated = len(file_content) > 12000
            note = ' (truncated to fit context window)' if was_truncated else ''
            # Replace the last user message with file context injected
            file_context = (
                f"The user has attached a file named '{file_name}'{note}.\n"
                f"File contents:\n```\n{truncated}\n```\n\n"
                f"User's instruction: {user_message}"
            )
            # Update the last message in ollama_messages (which is the current user msg)
            ollama_messages[-1]['content'] = file_context

        # Use llava (vision model) if image attached, otherwise tinydolphin
        image_data = request.data.get('image_data', '').strip()
        image_mime = request.data.get('image_mime', 'image/jpeg').strip()

        if image_data:
            # Inject image into the last user message for llava
            ollama_messages[-1]['images'] = [image_data]
            use_model = 'llava'
        else:
            use_model = 'tinydolphin'

        try:
            response = ollama.chat(
                model=use_model,
                messages=ollama_messages
            )
            sky_reply = response.message.content

        except Exception as e:
            return Response({"response": f"SKY Core Failure: {str(e)}"}, status=500)

        # Step 4: Save SKY's reply to the database
        ChatMessage.objects.create(
            session=session,
            role='assistant',
            content=sky_reply
        )

        return Response({"response": sky_reply})

class SkyHistoryAPI(APIView):
    """Returns full chat history for the current session — used to sync across devices"""

    def get(self, request):
        session_id = request.session.get('sky_session_id')
        if not session_id:
            return Response({'messages': []})
        try:
            session = ChatSession.objects.get(session_id=session_id)
            messages = [
                {
                    'role': msg.role,
                    'content': msg.content,
                    'timestamp': msg.timestamp.strftime('%I:%M %p')
                }
                for msg in session.messages.all()
            ]
            return Response({'messages': messages})
        except ChatSession.DoesNotExist:
            return Response({'messages': []})