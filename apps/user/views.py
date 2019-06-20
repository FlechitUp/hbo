from django.shortcuts import redirect, render
#from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, instance=request.user.userprofileinfo)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _(
            #    'Your profile was successfully updated!'))
            return render(request, 'initpage/index.html')
        else:
            #messages.error(request, _('Please correct the error below.'))
            return render(request, 'initpage/index.html')
            
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofileinfo)
        return render(request, 'register/index.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
