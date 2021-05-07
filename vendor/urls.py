from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('become-vendor/', views.become_vendor, name='become_vendor'),
	path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('edit-vendor/', views.edit_vendor , name='edit_vendor'),
	path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'),name='login'),
	path('add-product/', views.add_product, name='add_product'),
	path('', views.vendors, name='vendors'),
	path('<int:vendor_id>/', views.vendor, name='vendor')
]
