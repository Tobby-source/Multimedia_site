from django.urls import path
from .views import media_list


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='mediaapp/login.html'), name='login'),

    # Signup page (you’ll create a view for this)
    path('signup/', views.signup, name='signup'),

    # Home page
    path('', views.home, name='home'),
]
