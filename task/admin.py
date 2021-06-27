from task.models import Albumzone, Bannerchange, Navchang
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

#navcahge
class NavAdmin(admin.ModelAdmin):
    list_display=('id','text', 'created_date')
    list_display_links=('id',)

admin.site.register(Navchang,NavAdmin)


#banner
class BannerAdmin(admin.ModelAdmin):
    def thumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))

    thumnail.short_description=('photos')

    list_display=('id','thumnail', 'created_date')
    list_display_links=('id',)

admin.site.register(Bannerchange,BannerAdmin)

#album
class AlbumAdmin(admin.ModelAdmin):
    def thumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.img.url))

    thumnail.short_description=('photos')

    list_display=('id','thumnail', 'created_date')
    list_display_links=('id',)
   
admin.site.register(Albumzone,AlbumAdmin)




