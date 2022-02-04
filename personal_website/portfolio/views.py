from django.shortcuts import render, redirect
from .models import Project, Skills
from .forms import CreateProjectForm, EditProjectForm, DeleteProjectForm


# Create your views here.
def home(request):
    skills_with_no_description = Skills.objects.filter(description='')
    skills_with_description = Skills.objects.exclude(description='')
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'skills_with_no_description': skills_with_no_description,
        'skills_with_description': skills_with_description,
    }
    return render(request, 'index.html', context)


def view_project(request, id):
    project = Project.objects.get(pk=id)
    context = {
        'project': project,
    }
    return render(request, 'view_project.html', context)


def create_project(request):
    form = CreateProjectForm()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'create_project.html', context)


def edit_project(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = EditProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EditProjectForm(instance=project)
    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'edit_project.html', context)


def delete_project(request, id):
    project = Project.objects.get(pk=id)
    form = DeleteProjectForm(request.POST, request.FILES, instance=project)
    if form.is_valid():
        project.thumbnail.delete(save=True)
        project.delete()
        return redirect('home')
    form = DeleteProjectForm(instance=project)
    context = {
        'form': form,
        'project': project
    }
    return render(request, 'delete_project.html', context)
