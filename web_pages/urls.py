from django.urls import path
from django.contrib.auth import views as auth_views
from web_pages.views import (IntroductionView, ProjectList, GalleryList)
urlpatterns = [
			path('hard/introduction/', IntroductionView.as_view(), name='intro'),
			path('hard/project/list/', ProjectList.as_view(), name='project_list'),
			path('hard/project/list/gallery/', GalleryList.as_view(), name='gallery_list'),
    ]