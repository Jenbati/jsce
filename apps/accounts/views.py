from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class Dashboard_View(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_author:
            return redirect("author_dashboard")
        else:
            messages.error(request, "Your role is not recognised. Please contact admin.")
            return HttpResponse("<h1> Access Denied </h1> ", status=403)  # We will define this view/page later
            
class Author_Dashboard_View(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_author:
            return render(request, 'account/dashboard_author.html', {'active_tab': 'dashboard'})
        messages.error(request, "Access Denied. You are not authorized to view this page.")
        return redirect('dashboard')
        
@login_required
def user_profile(request):
    return render(request, 'account/profile.html', {'user': request.user, 'active_tab':'user_profile'})

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile was updated successfully!')
#             return redirect('user_profile')
#         else:
#             messages.error(request, 'Error updating your profile. Please check your input.')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     return render(request, 'account/profile_edit.html', {'form': form, 'active_tab': 'user_profile'})