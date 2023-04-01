
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings
from shop.admin import product_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productadmin/', product_admin_site.urls),
    path('account/', include('account.urls')),
    path('', include('shop.urls')),
    path('', include('checkout.urls')),
    path('', include('administration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
