from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


@unauthenticated_user
def landingPage(request):
    context = {}
    return render(request, 'accounts/landing.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def homeStudent(request):
    context = {}
    return render(request, 'accounts/dashboard_student.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def homeTeacher(request):
    context = {}
    return render(request, 'accounts/dashboard_teacher.html', context)


def logoutUser(request):
    logout(request)
    return redirect('landing')


@unauthenticated_user
def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group_name = user.groups.all()[0].name if user.groups.all() else 'No group'

            if group_name == 'teacher':
                return redirect('homeTeacher')
            elif group_name == 'student':
                return redirect('homeStudent')
            else:
                messages.info(request, 'Your group does not have access to this application')
                return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def registerStudent(request):
    form = CreateStudentForm()
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)
            Student.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account created: ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register_student.html', context)


@unauthenticated_user
def registerTeacher(request):
    form = CreateTeacherForm()
    if request.method =='POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            Teacher.objects.create(
                user=user,
                firstname="Firstname",
                lastname="Lastname",
                phone="",
            )

            messages.success(request, 'Account created: ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register_teacher.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher', 'student'])
def accountSettings(request):
    if request.user.groups.all()[0].name == 'teacher':
        teacher = request.user.teacher
        user = request.user
        form = TeacherForm(instance=teacher, initial={'user_email': user.email})
        email = user.email
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                teacher = form.save()
                email = form.cleaned_data['user_email']
                print(email)
                User.objects.filter(id=user.id).update(email=email)
                messages.info(request, 'Data successfully saved')

    elif request.user.groups.all()[0].name == 'student':
        student = request.user.student
        user = request.user
        form = StudentForm(instance=student, initial={'user_email': user.email})
        email = user.email

        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES, instance=student)
            if form.is_valid():
                student = form.save()
                email = form.cleaned_data['user_email']
                User.objects.filter(id=user.id).update(email=email)
                messages.info(request, 'Data successfully saved')
                messages.error(request, 'Error in saving data')
                messages.success(request, 'Data successfully saved')
    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)
