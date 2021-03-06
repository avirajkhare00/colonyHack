"""colony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app1.views import IndexView, CreateProjectView, GetProjects, ProjectDetailsView, ProjectFunds

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_page'),
    url(r'^project_details\/[0-9]{1,}$', ProjectDetailsView.as_view(), name='project_details_view'),
    url(r'^funds/$', ProjectFunds.as_view(), name='project_funds'),
    url(r'^api/v1/createProject/$', CreateProjectView.as_view(), name='create_project'),
    url(r'^api/v1/getProjects/$', GetProjects.as_view(), name='get_projects')

]
