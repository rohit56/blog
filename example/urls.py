from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', home, name='home'),
    url(r'^blog/', include('blog.urls', app_name='blog', namespace='blog')),
    url(r'^login/', user_login, name="user_login"),
    url(r'^logout/', user_logout, name="user_logout"),
    url(r'^register/', user_register, name="user_register"),
    url(r'^final/', final, name="final"),
]
