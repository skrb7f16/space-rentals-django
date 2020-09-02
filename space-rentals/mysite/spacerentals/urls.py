from django.urls import path,include
from spacerentals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="home"),
    path('pgList', views.pgList,name="pgList"),
    path('pgName', views.pgName,name="pgName"),
    path('booking', views.booking,name="booking"),
    path('logoutUser',views.logoutUser,name="logoutUser")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

