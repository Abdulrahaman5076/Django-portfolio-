from django.contrib import admin
from .models import About, Project, Skill, Certificate, Blog, Contact
from .models import Project

admin.site.site_header = "Abdulrahaman Portfolio Admin"
admin.site.site_title = "Portfolio Dashboard"
admin.site.index_title = "Welcome to the Portfolio Admin"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")



