from django.contrib import admin
from city.models import Province, City



class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
admin.site.register(Province, ProvinceAdmin)



class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ['name', 'province']
    list_filter = ("province",)
    raw_id_fields = ('province'),
admin.site.register(City, CityAdmin)

