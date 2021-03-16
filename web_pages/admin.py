from django.contrib import admin
from web_pages.models import Project, ProjectGallery

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_title','theme', 'donor','project_value','start_date', 'end_date', 'area', 'achievements', 'date'
    )

class ProjectPhotoGalleryAdmin(admin.ModelAdmin):
    list_display = (
        'shop_image','description'
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectGallery, ProjectPhotoGalleryAdmin)


