
from django.shortcuts import render
from projects.models import Project

# Create your views here.
def home(request):
    all_projects = Project.objects.all()
    num_projects = all_projects.count()
    return render(request, 'projects/project.html', {'all_projects':all_projects, 'num_projects':num_projects})
