from django.db import models

# define User-table
class User(models.Model):
    #id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64, null=false)
    last_name = models.CharField(max_length=64, null=false)
    password = models.CharField(max_length=128, null=false)
    email = models.CharField(max_length=64, null=false)
    profile_picture = models.CharField(max_length=64)
    
    
# define Kitchen-table
class Kitchen(models.Model):
    #id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=64, null=false)
    name = models.CharField(max_length=64, null=false)
    fridges = models.IntegerField(default=0)
    ovens = models.IntegerField(default=0)
    stoves = models.IntegerField(default=0)
    
    
# define Members-relation
class Members(models.Model):
    user_id= models.OneToOneField(
        User, on_delete=models.CASCADE)
    kitchen_id= models.OneToOneField(
        Kitchen, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user_id', 'kitchen_id'),)
    
    
# define Fridge-table
class Fridge(models.Model):
    #id = models.AutoField(primary_key=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)
    
    
# define Shelf-table
class Shelf(models.Model):
    #id = models.AutoField(primary_key=True)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)    
    
# define Cell-table
class Cell(models.Model):
    #id = models.AutoField(primary_key=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)  

# define Oven-table
class Oven(models.Model):
    #id = models.AutoField(primary_key=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)
    free = models.BooleanField(default=True)
    
# define Stoves-table
class Stove(models.Model):
    #id = models.AutoField(primary_key=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    type = models.CharField(max_length=64, null=False)
    free = models.BooleanField(default=True)
