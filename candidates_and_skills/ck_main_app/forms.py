from django import forms

from .models import SkillTag, SkillValue


class NewSkillForm(forms.ModelForm):
    class Meta:
        model = SkillValue
        fields = ('name', 'tag')
