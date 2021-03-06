from django.contrib import admin
from notes.models import Blogpost
from notes.models import CarouselImage 
from notes.models import Product
from notes.models import BlogCategory 
# Register your models here.
admin.site.register(Blogpost)
admin.site.register(BlogCategory)
admin.site.register(CarouselImage)
admin.site.register(Product)

class BlogpostAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        instance.owner = request.user
