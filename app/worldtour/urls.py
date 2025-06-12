from django.urls import path
from . import views

urlpatterns = [
    # Add your app's URLs here
    # Example:
    # path('example/', include('app.example.urls')),
    
    # Include the admin URLs
    # path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('static-assets/', views.static_assets),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    
]