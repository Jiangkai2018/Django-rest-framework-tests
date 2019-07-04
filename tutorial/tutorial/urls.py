# tutorial/urls.py
from django.urls import include, path
from rest_framework import routers
# from tutorial.quickstart import views
from quickstart import views
# 通过简单地使用路由器类注册视图集来自动为我们的API生成URL conf
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # 包含默认登录和注销,身份验证
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('root-snippets/', include('snippets.urls')),
]