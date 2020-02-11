from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from .models import Video
from django import forms


class VideoAdminChangeFrom(forms.ModelForm):
    class Meta(object):
        model = Video
        exclude = ()


class VideoAdmin(FileAdmin):
    form = VideoAdminChangeFrom


VideoAdmin.fieldsets = VideoAdmin.build_fieldsets(extra_main_fields=('poster', 'muted'))

admin.site.register(Video, VideoAdmin)  # use the standard FileAdmin
