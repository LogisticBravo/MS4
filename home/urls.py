import debug_toolbar

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.index, name='home'),
]
