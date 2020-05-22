from django.test import TestCase
from .models import Image,Location,Category

# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.new_location=Location(location="place")
#         self.new_location.save_location()

#         self.new_category=Category(category="food")
#         self.new_category.save_category()

#         self.new_image= Image(image="default.jpg",image_name ="trip",image_description="Some many words",image_location = self.new_location,image_category=self.new_category)
#         self.new_image.save()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_image,Image)) 

# class LocationTestClass(TestCase):
