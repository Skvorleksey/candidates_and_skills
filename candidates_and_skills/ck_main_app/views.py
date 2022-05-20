from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SkillTag, SkillValue
from django.contrib.auth.decorators import login_required
from .forms import NewSkillForm
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.
def users_view(request):
    """Index page view"""
    users = User.objects.filter(is_staff=False)
    context = {'users': users}
    return render(request, 'ck_main_app/index.html', context)


def user_details(request, user_id):
    """Info about chosen user"""
    user = User.objects.get(id=user_id)
    skill_tags = user.skilltag_set.all()
    skills = user.skillvalue_set.all()

    context = {
        'user': user,
        'skill_tags': skill_tags,
        'skills': skills,
    }
    return render(request, 'ck_main_app/user_details.html', context)


@login_required
def your_account(request):
    """Back office view"""
    user = request.user
    skill_tags = user.skilltag_set.all()
    skills = user.skillvalue_set.all()

    context = {
        'user': user,
        'skill_tags': skill_tags,
        'skills': skills,
    }
    return render(request, 'ck_main_app/your_account.html', context)


@login_required
def add_skills(request):
    """Form for adding skills"""
    if request.method != 'POST':
        form = NewSkillForm()
    else:
        form = NewSkillForm(data=request.POST)
        if form.is_valid():
            new_skill = form.save(commit=False)
            new_skill.save()
            new_skill.user.add(request.user)
            new_skill.tag.user.add(request.user)
            return redirect('ck_main_app:your_account')
    context = {'form': form}
    return render(request, 'ck_main_app/new_skill.html', context)
