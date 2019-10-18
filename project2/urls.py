
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from project2 import settings

urlpatterns = [
    path('school/', include('school.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', RedirectView.as_view(url='school/')),
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
