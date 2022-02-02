from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalog/', include('catalog.urls')),
    path('customers/', views.customers, name='customers'),
    path('analysis/', views.analysis, name='analysis'),
    path('branches/', views.branches, name='branches'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
