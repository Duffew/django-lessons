"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from hello_world import views as index_views
# Following the format we used to import our index views, 
# import views from about and alias them as about_views.
from about import views as about_views

# Django checks each of the URLs in the urls.py file in order. 
# For this simple project, it does not matter whether hello/ is above or below admin/. 
# For more complex projects, though, you may need to give attention to the order in which your URLs appear. 
# For the moment, just remember to keep admin/ at the bottom, as shown.
urlpatterns = [
    path('hello/', index_views.index, name='index'),
    # Now add a path to the urlpatterns. The path should be 'about/'.
    # The second argument should follow a similar format to our homepage. 
    # Check the about/views.py file again if you need to see what the function is called. 
    # Give it the name of 'about'.
    path('about/', about_views.about_me, name='about'),
    path('admin/', admin.site.urls),
]
