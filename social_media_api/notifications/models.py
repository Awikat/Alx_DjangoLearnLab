from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from posts.models import Post

# Create your models here.

User = get_user_model()
class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, related_name='actor_notifications', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_content_type = models.ForeignKey(ContentType, related_name='target_object', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    target = GenericForeignKey('target_content_type','post')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.actor} {self.verb} {self.target} to {self.recipient}'
