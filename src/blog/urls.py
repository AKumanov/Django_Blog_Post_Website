from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site


from posts.views import (
        index, blog, post, post_create, search, 
        post_update, post_delete, view_more)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('view_more/', view_more, name='view_more')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
