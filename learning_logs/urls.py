"""define url of learning_logs"""
from django.conf.urls import url

from . import views

urlpatterns = [
	# home page of learning_logs
	url(r'^$', views.index, name='index'),

	# topics page
	url(r'^topics/$', views.topics, name='topics'),

	# page for specific topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# new topic page
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# new entry page
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# page where user can edit entries
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]