from django.contrib import admin
from django.urls import path, include
from rental.api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/v1/', include(router.urls)),
]
