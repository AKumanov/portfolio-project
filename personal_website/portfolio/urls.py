from django.urls import path
from .views import create_project, edit_project, delete_project, \
    view_project, inbox, message, loginPage, logoutPage, registerPage

from personal_website.portfolio.views import home

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
    path('project/<int:id>', view_project, name='project details'),
    path('project/edit/<int:id>', edit_project, name='edit project'),
    path('project/add/', create_project, name='add project'),
    path('project/delete/<int:id>', delete_project, name='delete project'),

    path('inbox/', inbox, name='inbox'),
    path('message/<int:id>', message, name='message'),

]
