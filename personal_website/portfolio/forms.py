from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add tittle...'}
        )
        self.fields['thumbnail'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add description...'}
        )

    class Meta:
        model = Project
        fields = '__all__'


class CreateProjectForm(ProjectForm):
    pass


class EditProjectForm(ProjectForm):
    pass


class DeleteProjectForm(ProjectForm):
    pass
