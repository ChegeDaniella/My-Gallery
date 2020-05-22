from django.test import TestCase
from .models import Image,Location,Category

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_image= Image(image_name ="trip",image_description="Some many words",image_location="mountains",image_category="food")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image)) 

# class LocationTestClass(TestCase):
