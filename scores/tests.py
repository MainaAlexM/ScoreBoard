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


class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(
            username='testerd',email='apptestermind@gmail.com',password='key_one'
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        user=User.objects.all()
        self.assertEquals(len(user),1)
    
    def test_delete_method(self):
        self.new_user.save()
        self.new_user.delete()
        user = User.objects.all()
        self.assertFalse(User.objects.filter(pk=self.new_user.id).exists())


class RatingsTestCase(TestCase):

    def setUp(self):
        self.user=User(
            username='prof',email='apptestermind@gmail.com',password='key_one'
    )
        self.image=Project(title='test_title',owner=self.user,landing_page='https://www.pexels.com/photo/portrait-of-beautiful-woman-posing-outdoors-12339648/200/300',description='Trial Message',site_url='https://pexels.com')

        self.user.save()
        self.image.save()
    def test_instance(self):
        self.project = Ratings(project = self.image,design = 5,usability=3,content=8,user=self.user)
        self.assertTrue(isinstance(self.project,Ratings))


