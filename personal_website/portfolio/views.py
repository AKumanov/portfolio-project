from django.shortcuts import render, redirect
from .models import Project, Skills, Message
from .forms import CreateProjectForm, EditProjectForm, \
    DeleteProjectForm, MessageForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    skills_with_no_description = Skills.objects.filter(description='')
    skills_with_description = Skills.objects.exclude(description='')
    projects = Project.objects.all()

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!')
    context = {
        'projects': projects,
        'skills_with_no_description': skills_with_no_description,
        'skills_with_description': skills_with_description,
        'form': form,
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
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


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {
        'page': page,
    }

    return render(request, 'login.html', context)


def registerPage(request):
    form = CustomUserCreationForm()
    page = 'register'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def inbox(request):
    inbox = Message.objects.all().order_by('is_read')

    unread_count = Message.objects.filter(is_read=False).count()
    context = {
        'inbox': inbox,
        'unread_count': unread_count,
    }
    return render(request, 'inbox.html', context)


def message(request, id):
    message = Message.objects.get(pk=id)
    message.is_read = True
    message.save()
    context = {
        'message': message,
    }
    return render(request, 'message.html', context)
