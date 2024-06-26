from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('accounts/', include('backend.accounts.urls')),  # without namespace
    path('accounts/', include('registration.backends.default.urls')),  # django-registration-redux
    path('admin/', admin.site.urls),
]
