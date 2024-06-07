from django.contrib import admin
from django.urls import path
from App1.views import m1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', m1.as_view(), name='mi_urls')
]
