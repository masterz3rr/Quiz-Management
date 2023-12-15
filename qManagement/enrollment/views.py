from django.shortcuts import render, redirect
from django.db import connection


def studentPage(request):
    student = request.user.student
    sID = student.id
    cursor = connection.cursor()
    args = [sID]
    cursor.callproc('studentClassList', args)
    results = cursor.fetchall();
    cursor.close()
    context = {'results': results}
    return render(request, 'enrollment/studentPage.html', context)
