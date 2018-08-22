from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^result/$', search, name='search'),
    url(r'^blog-list/$', post_list, name='blog_list'),
    url(r'^blog-detail/(?P<slug>[-\w]+)/$', post_detail, name='blog_detail'),
    url(r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name='category_detail'),

    url(r'^new-post/$', new_post, name='new_post'),

    url(r'^post-list/$', post_list_admin, name='post_list_admin'),
    url(r'^edit-post/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    url(r'^delete-post/(?P<pk>\d+)/$', delete_post, name='delete_post'),
]

