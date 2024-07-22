from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
admin.site.site_header = 'Foodee Admin'
urlpatterns = [
   path('base/',views.BASE,name='base'),
   path('', views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
