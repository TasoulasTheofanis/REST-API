from django.contrib import admin
from api import models #from the api folder

admin.site.register(models.UserProfile) #register the UserProfile model with the admin
