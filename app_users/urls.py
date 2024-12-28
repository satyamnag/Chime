from typing import Any
from django.urls import path
from app_users.views import *
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin

class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView, PasswordChangeDoneView):
    template_name = 'app_users/password_change_form.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['current_user']=self.request.user
        return context

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='app_users/logout.html'), name='logout'),
    path('', index, name='index'),
    path('password_change/', MyPasswordChangeView.as_view(template_name='app_users/password_change_form.html'), name='password_change'),
    path('password_change_done/', MyPasswordChangeView.as_view(template_name='app_users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='app_users/password_reset_form.html'), name='password_reset'),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='app_users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='app_users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='app_users/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('TNC/', tnc, name='tnc'),
    path('PP/', pp, name='pp'),
]