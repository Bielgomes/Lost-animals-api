from django.contrib import admin

from animals.models import Animal, Breed, Type

admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Type)
