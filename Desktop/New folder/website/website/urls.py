from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^program', views.program, name='program'),
    url(r'^lists', views.lists, name='lists'),
    url(r'^alumni', views.alumni, name='alumni'),
    url(r'^faculty', views.faculty, name='faculty'),
    url(r'^research', views.research, name='research'),
    url(r'^Research/(?P<pk>\d+)$', views.research_item, name='research_item'),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^outreach', views.outreach, name='outreach'),
    url(r'^Outreaches/(?P<pk>\d+)$', views.item_outreach, name='outreach_item'),
    url(r'^news', views.news, name='news'),
    url(r'^upcomingevents', views.upcomingevents, name='upcomingevents'),
    url(r'^News/(?P<pk>\d+)$', views.news_item, name='news_item'),
    url(r'^education', views.education, name='education'),
    url(r'^business', views.business, name='business'),
    url(r'^administration', views.administration, name='administration'),
    url(r'^management', views.management, name='management'),
    url(r'^computer_studies', views.computer_studies, name='computer_studies'),
    url(r'^criminal_justice', views.criminal_justice, name='criminal_justice'),
    url(r'^psychology', views.psychology, name='psychology'),
    url(r'^nursing', views.nursing, name='nursing'),
    url(r'^Programs/(?P<pk>\d+)$', views.program_item, name='program_item'),
    url(r'^login', views.login, name='login'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^postlist/(?P<string>[\w\-]+)/$', views.postlist, name='postlist'),
    url(r'^search', views.search, name='search'),

]