from django.shortcuts import render, redirect
from django.db import connection
from createQuiz.models import ClassList
from django.contrib import messages
import datetime


def studentPage(request):
    student = request.user.student
    sID = student.id
    cursor = connection.cursor()
    args = [sID]
    cursor.callproc('studentClassList', args)
    results = cursor.fetchall();
    cursor.close()

    cursor = connection.cursor()
    cursor.execute("SELECT C.* FROM createquiz_classlist AS C LEFT JOIN enrollment_enrolledclasses AS E ON C.classID = E.classID_id AND E.studentID_id = %s WHERE E.studentID_id IS NULL;", [sID])
    resultList = cursor.fetchall()
    cursor.close()
    context = {'results': results, 'resultList': resultList}
    return render(request, 'enrollment/studentPage.html', context)


def enrollClassInfo(request, id):
    classData = ClassList.objects.get(classID=id)
    cursor = connection.cursor()
    cursor.execute("SELECT * from accounts_teacher WHERE id = %s;", [classData.teacherID_id])
    result = cursor.fetchall()
    cursor.close()
    if request.method == 'POST':
        if classData.enrollKey == request.POST['enrollkey']:
            dEnroll = datetime.datetime.now()
            cID = classData.classID
            student = request.user.student
            sID = student.id
            result = ""
            cursor = connection.cursor()
            args = [dEnroll, cID, sID, result]
            print(args)
            cursor.callproc('enrollClass', args)
            result = cursor.fetchall()
            msg = result[0][0]
            cursor.close()
            return redirect('/student/')
        else:
            messages.error(request, 'No changes applied')
    context = {'classData': classData, 'result': result}
    return render(request, 'enrollment/enrollClassInfo.html', context)


def studentClassView(request, id):
    classData = ClassList.objects.get(classID=id)
    cursor = connection.cursor()
    cursor.execute("SELECT A.quizID,B.topicID,A.quizName,A.quizDescription,B.topicName,b.topicDescription FROM `createquiz_quizlist` as A JOIN `createquiz_topiclist` as B on A.topicID_id = B.topicID JOIN `createquiz_classlist` as C on B.classID_id = C.classID WHERE B.classID_id = %s;", [id])
    results = cursor.fetchall()
    cursor.close()

    context = {'classData': classData, 'results': results}
    return render(request, 'enrollment/studentClassView.html', context)


def studentExam(request, id):
    context = {}
    return render(request, 'enrollment/studentExam.html', context)
