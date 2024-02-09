from django.contrib import admin
from teacher.models import Teacher, ReserveTimes




class ReserveTimesInline(admin.TabularInline):
    model = ReserveTimes
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('cover','user', 'name', 'id')
    inlines = [ReserveTimesInline, ]
admin.site.register(Teacher, TeacherAdmin)

