
from rest_framework import viewsets
from common_lib.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from common_lib.response import SuccessResponse
from operation.models import (
    Color,
    TagCategory,
    Tag,
    Group,
    User,
    UserRegisted,
)
from operation.serializers import (
    ColorSerializer,
    TagCategorySerializer,
    TagSerializer,
    GroupSerializer,
    UserSerializer,
    UserRegistedSerializer,
)


class ColorViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    '''
        list: Return all colors,ordered by most recent joined.
        create: Create a new color.
        delete: Remove a existing color.
        partial_update: Update one or more fields on a existing color.
        update: Update a color.
    '''
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TagCategoryViewSet(viewsets.ModelViewSet):
    '''
        retrieve: Return a category instance.
        list: Return all categories,ordered by most recent joined.
        create: Create a new category.
        delete: Remove a existing category.
        partial_update: Update one or more fields on a existing category.
        update: Update a category.
    '''
    queryset = TagCategory.objects.all()
    serializer_class = TagCategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    '''
        retrieve: Return a tag instance.
        list: Return all tags,ordered by most recent joined.
        create: Create a new tag.
        delete: Remove a existing tag.
        partial_update: Update one or more fields on a existing tag.
        update: Update a tag.
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''
        retrieve: Return a group instance.
        list: Return all groups,ordered by most recent joined.
        create: Create a new group.
        delete: Remove a existing group.
        partial_update: Update one or more fields on a existing group.
        update: Update a group.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
        retrieve: Return a user instance.
        list: Return all users,ordered by most recent joined.
        create: Create a new user.
        delete: Remove a existing user.
        partial_update: Update one or more fields on a existing user.
        update: Update a user.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistedViewSet(viewsets.ModelViewSet):
    '''
        retrieve: Return a userRegisted instance.
        list: Return all userRegisteds,ordered by most recent joined.
        create: Create a new userRegisted.
        delete: Remove a existing userRegisted.
        partial_update: Update one or more fields on a existing userRegisted.
        update: Update a userRegisted.
    '''
    queryset = UserRegisted.objects.all()
    serializer_class = UserRegistedSerializer
