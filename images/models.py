from django.db import models
 

class Image(models.Model):
   
    image_name = models.CharField(max_length = 60)
    image_description = models.TextField (max_length = 500)
    image_location = models.CharField(max_length = 60)
    image_category = models.CharField(max_length = 60)
