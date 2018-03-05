"""watchshopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from watchshopapp import views, apis
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('watchshop/sign-in/', auth_views.login,
         {'template_name': 'watchshop/sign_in.html'},
         name='watchshop-sign-in'),
    path('watchshop/sign-out/', auth_views.logout, {'next_page': '/'}, name='watchshop-sign-out'),
    path('watchshop/', views.watchshop_home, name='watchshop-home'),
    path('watchshop/sign-up/', views.watchshop_sign_up, name='watchshop-sign-up'),
    path('watchshop/account/', views.watchshop_account, name='watchshop-account'),
    path('watchshop/watch/', views.watchshop_watch, name='watchshop-watch'),
    path('watchshop/watch/add/', views.watchshop_add_watch, name='watchshop-add-watch'),
    path('watchshop/watch/edit/<int:watch_id>/', views.watchshop_edit_watch, name='watchshop-edit-watch'),

    #APIs
    path('api/client/watchshops/', apis.client_get_watchshops),
    path('api/client/watchs/<int:watchshop_id>/', apis.client_get_watchs),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
