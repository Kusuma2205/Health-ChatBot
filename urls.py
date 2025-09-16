from django.urls import path, include

urlpatterns = [
    path('api/', include('chat.urls')),  # change chatbot to your app name
]
