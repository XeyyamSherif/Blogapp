from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from examples import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.basepage),
                  path('mainpage/', views.mainpage),
                  path('signup/', views.signuppage),
                  path('login/', views.loginpage),
                  path('signin/', views.login),
                  path('logout/', views.logut),
                  path('add_img/', views.add_img),
                  path('usersettings/', views.usersettings),
                  path('update/', views.update_user),
                  path("sagol/", views.basepage),
                  path('postdetail/<int:post_id>/', views.post_detail),
                  path('addcomment/<int:post_id>/', views.add_comment),
                  path('deletecomment/<int:comment_id>/', views.delete_comment),
                  path('ajax/just/', views.just)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
