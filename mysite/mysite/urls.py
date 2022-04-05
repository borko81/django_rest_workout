from itertools import product
from django.contrib import admin
from django.urls import path, include
from rental.api import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/v1/', include(router.urls)),
    path('app/auth/', include('djoser.urls.authtoken')),
    path('api/', include('app.urls')),
    path('products/', include('products.urls')),
    path('toys/', include('toys.urls'))
]
