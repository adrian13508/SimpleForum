
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views 

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', include('quickstart.urls', namespace='post_list')),
    path('posts/', views.PostViewSet.as_view({'get': 'list'})),
    path('posts/<int:id>', views.PostViewSet.as_view({'get': 'list'})),

]
