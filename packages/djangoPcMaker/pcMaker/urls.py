from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home ,name='home'),
    path('motherBoard/', views.motherBoard, name='motherBoard'),
    path('gpu/', views.gpu, name='gpu'),
    path('stockage/', views.stockage, name='stockage'),
    path('processeur/', views.processeur, name='processeur'),
    path('ram/', views.ram, name='ram'),
    path('ordinateur/', views.ordinateur, name='ordinateur'),
    path('ordinateur/delete/<int:param>', views.ordinateurIC, name='delOrdinateur'),
    path('ram/delete/<int:param>', views.deleteIC, name='delRam'),
    path('gpu/delete/<int:param>', views.deleteIC, name = 'delGpu'),
    path('motherBoard/delete/<int:param>', views.deleteIC, name='delMotherBoard'),
    path('processeur/delete/<int:param>', views.deleteIC, name = 'delCpu'),
    path('stockage/delete/<int:param>', views.deleteIC, name='delStockage'),
    path('gpu/update/<int:param>', views.updateIC, name='updateGpu'),
    path('motherBoard/update/<int:param>', views.updateIC, name='updateMotherBoard'),
    path('processeur/update/<int:param>', views.updateIC, name='updateProcesseur'),
    path('ordinateur/update/<int:param>', views.ordinateurIC, name='updateOrdinateur'),
    path('ram/update/<int:param>', views.updateIC, name='updateRam'),
    path('stockage/update/<int:param>', views.updateIC, name='updateStockage'),
    path('ordinateur/configs/', views.myConfigsIC, name='configs'),
    
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', views.exit, name="logout")
] 