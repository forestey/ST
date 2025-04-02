# 定义learning_logs的URL模式

from django.urls import re_path
from . import views


urlpatterns = [
    # 主页
    re_path(r'^$', views.index, name='index'),

    # Show all topics.
    re_path(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic.
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页
    re_path(r'^new_topic/$', views.new_topic, name='new_topic')
]