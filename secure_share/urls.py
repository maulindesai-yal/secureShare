from django.contrib import admin
from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    path('upload_new_document/', home_views.upload_new_document, name='upload_new_document'),
    path('view_all_documents/', home_views.view_all_documents, name='view_all_documents'),


]