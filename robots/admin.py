from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin

from .models import *


class BackupInline(NestedTabularInline):
    model = Backup
    extra = 1
    # fk_name = 'level'


class ServiceInline(NestedStackedInline):
    model = Service
    extra = 1
    # fk_name = 'level'
    inlines = [BackupInline]


class RobotAdmin(NestedModelAdmin):
    inlines = [ServiceInline]


class ServiceAdmin(NestedModelAdmin):
    inlines = [BackupInline]


admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Integrator)
admin.site.register(Arm)
admin.site.register(Backup)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Controller)
admin.site.register(Robot, RobotAdmin)
