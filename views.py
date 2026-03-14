import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import ollama

def index(request):
    """Renders the SKY Terminal Interface"""
    return render(request, 'sky_app/index.html')

class SkyChatAPI(APIView):
    """Local brain of SKY using TinyDolphin"""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        message = request.data.get('message')
        
        if not message:
            return Response({"response": "System awaiting command, sir."}, status=400)

        try:
            # Ensure you ran 'ollama pull tinydolphin' in your terminal
            response = ollama.chat(model='tinydolphin', messages=[
                {
                    'role': 'system',
                    'content': 'Your name is SKY. You are a fast, efficient AI assistant. Keep responses brief and professional. Address the user as Sir.'
                },
                {
                    'role': 'user',
                    'content': message,
                },
            ])
            
            ai_text = response['message']['content']
            return Response({"response": ai_text})
            
        except Exception as e:
            return Response({"response": f"SKY Core Failure: {str(e)}"}, status=500)