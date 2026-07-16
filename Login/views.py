import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Student


# ---------- PAGES (return HTML) ----------

def login_page(request):
    # If already logged in, skip the login page
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "login.html")


@login_required(login_url="/")  # not logged in? go back to the login page
def dashboard(request):
    return render(request, "dashboard.html")


# ---------- AUTH API (return JSON) ----------

def login_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # authenticate() checks username + password against the database.
        # It returns the User if correct, or None if wrong.
        user = authenticate(
            request,
            username=data["username"],
            password=data["password"],
        )

        if user is None:
            return JsonResponse({"message": "Invalid username or password"}, status=401)

        # login() saves the user in the session (a cookie),
        # so Django remembers them on every next request.
        login(request, user)
        return JsonResponse({"message": f"Welcome back, {user.username}!"})


def register_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if User.objects.filter(username=data["username"]).exists():
            return JsonResponse({"message": "That username is already taken"}, status=400)

        # create_user() hashes the password before saving —
        # never store plain-text passwords!
        user = User.objects.create_user(
            username=data["username"],
            password=data["password"],
        )

        login(request, user)  # log them in right away
        return JsonResponse({"message": f"Account created. Welcome, {user.username}!"}, status=201)


def logout_api(request):
    logout(request)  # clears the session
    return JsonResponse({"message": "Logged out"})


# ---------- STUDENT API (from the earlier lesson) ----------

@csrf_exempt
def student_api(request):

    if request.method == "GET":
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)

        student = Student.objects.create(
            name=data["name"],
            age=data["age"],
            email=data["email"],
            course=data["course"],
        )

        return JsonResponse(
            {
                "message": "Student created successfully",
                "id": student.id,
            },
            status=201,
        )
