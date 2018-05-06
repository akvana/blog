from django.contrib import admin

# Register your models here.
from .models import  Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','publising_Date']
    list_display_links=['publising_Date']
    list_filter=['publising_Date']
    search_fields=['title','content']
    list_editable=['title']
    class Meta:
        model=Post


admin.site.register(Post,PostAdmin)
