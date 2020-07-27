from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def homepage(request):
    jobs = Job.objects
    details = Detail.objects
    skills = Skill.objects
    projects = Project.objects
    educations = Education.objects
    return render(request, 'jobs/home.html', {'jobs':jobs,'details':details, 'skills':skills, 'projects':projects, 'educations':educations})
