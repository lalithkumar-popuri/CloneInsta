from django.db import models
from django.urls import reverse
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'posts')
    created_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='media/')
    caption = models.TextField()
    caption_html = models.TextField(editable = False)

    def __str__(self):
        return self.user
    def save(self, *args, **kwargs):
        self.caption_html = misaka.html(self.caption)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse(
            "posts:all")
    class Meta:
        ordering = ["-created_at"]
