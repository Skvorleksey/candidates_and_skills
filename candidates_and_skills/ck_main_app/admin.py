from django.contrib import admin
from .models import SkillTag, SkillValue


# Register your models here.
class SkillTagAdmin(admin.ModelAdmin):
    fields = ['name', 'user']
    list_display = ('name', 'get_users')


class SkillValueAdmin(admin.ModelAdmin):
    fields = ['name', 'tag', 'user']
    list_display = ('name', 'tag', 'get_users')


admin.site.register(SkillTag, SkillTagAdmin)
admin.site.register(SkillValue, SkillValueAdmin)
