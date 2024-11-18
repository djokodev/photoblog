from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

from authentication.views import signup_page, upload_profile_photo
from blog.views import home, photo_upload, blog_and_photo_upload, view_blog, edit_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
        name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
        name='password_change_done'
         ),
    path('signup/', signup_page, name='signup'),
    path('blog/create', blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit', edit_blog, name='edit_blog'),
    path('profile-photo/upload', upload_profile_photo, name='upload_profile_photo'),
    path('home/', home, name='home'),
    path('photo/upload/', photo_upload, name='photo_upload'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
