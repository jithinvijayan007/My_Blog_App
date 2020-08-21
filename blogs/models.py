from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=128)
    Content = models.TextField()
    Date_Of_Upload = models.DateTimeField(default=timezone.now)
    Image = models.ImageField(default="default.jpg",upload_to="profile_pics",blank="True")
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("list")
