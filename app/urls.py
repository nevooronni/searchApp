from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
	url('^$',views.index,name = 'index'),
	url(r'^article/(\d+)',views.article,name='article'),
	url(r'^search/',views.search_results,name='search_results')
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
