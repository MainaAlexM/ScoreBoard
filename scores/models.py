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


class Project(models.Model):
    title = models.CharField(max_length=60, blank=False)
    landing_page = CloudinaryField("landing_page")
    site_url = models.URLField()
    description = models.TextField()
    owner = models.ForeignKey(
        User, related_name="projects", null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def save_project(cls, project):
        cls.save()

    @classmethod
    def delete_prject(cls, project_id):
        cls.delete(id=project_id)

    @classmethod
    def update_project(cls, title):
        cls.update(title=title)

    @classmethod
    def search_project(cls, title):
        project = cls.objects.filter(title__icontains=title)
        return project


class Ratings(models.Model):
    project = models.ForeignKey(
        Project, related_name="ratings", on_delete=models.CASCADE)
    design = models.IntegerField(null=True)
    usability = models.IntegerField(null=True)
    content = models.IntegerField(null=True)
    user = models.ForeignKey(User, related_name="users",
                            on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"Design: {self.design} Usability: {self.usability} Content: {self.content}"