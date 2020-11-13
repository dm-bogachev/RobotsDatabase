from django.contrib import admin
from .models import *


class WorkingDatePartInline(admin.TabularInline):
    model = WorkingDayPart


class WorkingDayAdmin(admin.ModelAdmin):
    inlines = [
        WorkingDatePartInline,
    ]


admin.site.register(WorkingDay, WorkingDayAdmin)
admin.site.register(WorkingPlace, WorkingDayAdmin)



