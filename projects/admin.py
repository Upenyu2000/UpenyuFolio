from django.contrib import admin
from .models import Folio, About, Project, Stack
from embed_video.admin import AdminVideoMixin

# Register your models here.
@admin.register(Folio)
class FolioAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('project_image', 'title', 'project_description', 'project_url')
    list_editable = ('title', 'project_description',)  # Allow 'title' field to be editable directly in the list display

@admin.register(About)
class AboutAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('about',)

@admin.register(Stack)
class StackAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title','language_image','framework_image',)

@admin.register(Project)
class ProjectAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('video', 'video_type', 'description')
    list_editable = ('description',)
