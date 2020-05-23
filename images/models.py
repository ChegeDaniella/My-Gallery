from django.db import models
 
class Location(models.Model):
    location = models.CharField(max_length = 40)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()    

class Category(models.Model):
    category = models.CharField(max_length = 40)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to='saved/',null=True)
    image_name = models.CharField(max_length = 60)
    image_description = models.TextField (max_length = 500)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']  

    def save_image(self):
        self.save() 

    def delete_image(self):
        self.delete()
        

    @classmethod
    def update_image(cls,name,update):
        Image.objects.filter(image_name=name).update(image_name=update)
        update=Image.objects.get(image_name=update)
        return update 

    def get_image_by_id(self,id):
        post = self.objects.get(pk=id)
        return post

    @classmethod
    def search_by_category(cls,category):
        posts = cls.objects.filter(image_category__icontains=category)
        return posts 

    @classmethod
    def filter_by_location(cls,location):
        image = cls.objects.filter(image_location=location)
        return image










