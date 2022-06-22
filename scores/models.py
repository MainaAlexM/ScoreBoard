from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    profile_image = CloudinaryField("profile_image")
    bio = models.TextField()
    user = models.OneToOneField(User,  related_name='profiles' ,on_delete=models.CASCADE)

    def _str_(self):
        return self.user.username

    @classmethod
    def update_profile(cls, username, email, bio, profile_image):
        cls.update(username=username, email=email,
                bio=bio, profile_image=profile_image)

    @classmethod
    def save_profile(cls, profile):
        cls.save(profile)

    @classmethod
    def delete_profile(cls, profile):
        cls.delete(profile)

