from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


router = routers.DefaultRouter()
# router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += format_suffix_patterns(
    [
        path("users/", views.UserList.as_view()),
        path("users/<int:pk>/", views.UserDetail.as_view()),
        path("snippets/", views.SnippetList.as_view()),
        path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
    ]
)

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]
