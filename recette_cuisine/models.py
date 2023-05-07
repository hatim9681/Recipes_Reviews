from django.db import models

from django.contrib.auth.models import User


# Create your models here.
#recette
class Recette(models.Model):
    nom = models.CharField(max_length=50)
    temps = models.IntegerField()
    preparation=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/")
    

    def __str__(self):
        return self.nom

#ingredient
class Ingredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.recette.nom
    


#review
class Review(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
   # rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
    