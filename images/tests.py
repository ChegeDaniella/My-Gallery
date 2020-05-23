from django.test import TestCase
from .models import Image,Location,Category

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location="place")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_location(self):
        self.new_location.save_location()    

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category=Category(category="food")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_category(self):
        self.new_category.save_category()            

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

    def test_save_image(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>0)    

    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)

    def test_update_image(self):
        update= Image.update_image(self.new_image.image_name,"new name")
        self.assertEqual(update.image_name,"new name")

    def test_filter_by_location(self):
        location = self.new_image.image_location
        find = self.new_image.filter_by_location(location) 
        self.assertTrue(location = find) 
          
    # def test_search_by _category(self):



        
          


