from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user).order_by('-timestamp')

    @action(detail=False, methods=['post'])
    def mark_as_read(self, request):
        notifications = self.get_queryset().filter(read=False)
        notifications.update(read=True)
        return Response({'status': 'notifications marked as read'}, status=status.HTTP_200_OK)
