
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('shop.urls')),
    path('', include('checkout.urls')),
    path('controller/', include('controller.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
