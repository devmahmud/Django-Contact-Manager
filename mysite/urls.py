from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('',include('contacts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# Customizing admin text
admin.site.site_header = "Contacts"
admin.site.index_title = "Welcome to project"
admin.site.site_title = "Control Panel"