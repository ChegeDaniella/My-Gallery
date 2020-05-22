from django.test import TestCase
from .models import Image,Location,Category

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location="place")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_location(self):
        self.new_location.save_location()    

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_location=Location(location="place")
        self.new_location.save_location()

        self.new_category=Category(category="food")
        self.new_category.save_category()

        self.new_image= Image(image="default.jpg",image_name ="trip",image_description="Some many words",image_location = self.new_location,image_category=self.new_category)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image)) 

    def tearDown(self):
        Image.objects.all().delete()  
        Location.objects.all().delete() 
        Category.objects.all().delete()   


