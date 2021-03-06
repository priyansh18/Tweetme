"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from hashtag.views import HashTagView
from tweet.views import TweetListView
from accounts.views import UserRegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='home'),
    url(r'^register/$', UserRegistrationView.as_view(), name='register'),
    url(r'^tweet/', include('tweet.urls')),
    url(r'^tags/', include(('hashtag.urls', 'hashtag'), namespace='hashtag')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^tweet/api/', include('tweet.api.urls')),

]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
