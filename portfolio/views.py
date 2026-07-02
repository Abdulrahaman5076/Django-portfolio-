from django.shortcuts import render
from .models import *

def home(request):
    context = {
    "about": About.objects.first(),
    "skills": Skill.objects.all(),
    "projects": Project.objects.all(),
    "certificates": Certificate.objects.all(),
    "blogs": Blog.objects.all(),
    }
    
    return render(request, "portfolio/index.html", context)