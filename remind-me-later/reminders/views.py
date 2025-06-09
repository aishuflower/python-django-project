from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderCreateAPIView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
