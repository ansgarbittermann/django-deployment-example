from django.db import models
#connect to USER database from admin
from django.contrib.auth.models import User
# Create your models here.

#extend the user module coming with Django
class UserProfileInfo(models.Model):

    #create relationship (don't inherit from User! just one2one mapping)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want
    #we add url to portfolio of user and picture
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    #decide of what should be shown in the admin model, we choose username
    def __str__(self):
        #built-in attribute of django.contrib.auth.models.User !
        return self.user.username
