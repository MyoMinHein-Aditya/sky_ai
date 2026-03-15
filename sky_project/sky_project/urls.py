from django.contrib import admin
from django.urls import path
from sky_app.views import index, SkyChatAPI, SkyHistoryAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/chat/', SkyChatAPI.as_view(), name='sky_api'),
    path('api/history/', SkyHistoryAPI.as_view(), name='sky_history'),
]