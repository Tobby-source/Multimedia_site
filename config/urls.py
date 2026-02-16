"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import auth views for login/logout
from django.contrib.auth import views as auth_views

# Import your views from mediaapp
from mediaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='mediaapp/login.html'), name='login'),

    # Signup page
    path('signup/', views.signup, name='signup'),

    # Home page
    path('', views.home, name='home'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
