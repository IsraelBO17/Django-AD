from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2/', include('django_auth_adfs.drf_urls')),
    path('api/v1.0/users/', include('accounts.urls')),
    # Swagger UI 
    path('api/v1.0/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1.0/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]