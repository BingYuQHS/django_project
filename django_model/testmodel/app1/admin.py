from django.contrib import admin

# Register your models here.
from .models import Person,Blog,Author,Entry

admin.site.register(Person)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
