from django.contrib import admin
from studyTime.models import Time

# Register your models here.


class TimeAdmin(admin.ModelAdmin):

    list_display = ('title', 'date', 'startTime', 'planningTime', 'endTime')


admin.site.register(Time, TimeAdmin)
