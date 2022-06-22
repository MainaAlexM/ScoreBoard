from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project,Ratings

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user=User(
            username='prof',email='apptestermind@gmail.com',password='key_one'
    )
        self.image=Project(title='test',owner=self.user,landing_page='https://www.pexels.com/photo/portrait-of-beautiful-woman-posing-outdoors-12339648/200/300',description='Trial Message',site_url='https://pexels.com')


        self.user.save()
        self.image.save()


    def test_save_profile(self):
        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)


