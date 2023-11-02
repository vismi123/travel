from django.contrib import admin
from .models import Place
# Register your models here.
from .models import People
admin.site.register(Place)
admin.site.register(People)


