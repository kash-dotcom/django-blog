from django.contrib import admin
from .models import AboutMe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


admin.site.register(AboutMe, AboutAdmin)
