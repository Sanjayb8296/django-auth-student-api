from django.urls import path

from .views import (
    login_page,
    dashboard,
    login_api,
    register_api,
    logout_api,
    student_api,
)

urlpatterns = [
    # Pages
    path("", login_page, name="login"),
    path("dashboard/", dashboard, name="dashboard"),

    # Auth API
    path("api/login/", login_api),
    path("api/register/", register_api),
    path("api/logout/", logout_api),

    # Student API (same URL as before: /api/students/)
    path("api/students/", student_api),
]
