from django.test import TestCase
from . models import Tutorial

# Create your tests here.

class TutorialTestClass(TestCase):

    def setUp(self):
        self.description=Tutorial(location='description')

    def test_instance(self):
        self.assertTrue(isinstance(self.description,Tutorial))

    def tearDown(self):
        Tutorial.objects.all().delete()

    def test_save_method(self):
        self.description.save_location()
        tutorial = Tutorial.objects.all()
        self.assertTrue(len(tutorial)>0)

    def test_delete_method(self):
        self.description.delete_location('description')
        projects = Projects.objects.all()
        self.assertTrue(len(projects)==0)