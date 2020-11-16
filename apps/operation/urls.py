from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(
    title='API', renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer])

router = DefaultRouter()

router.register(r'colors', views.ColorViewSet)
router.register(r'categorys', views.TagCategoryViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    re_path('docs/', schema_view, name='docs')
]
