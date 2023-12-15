from django.shortcuts import render, redirect
from django.db import connection
from .forms import *
from django.contrib import messages
import random
import string


# Create your views here.
def classPage(request):
    teacher = request.user.teacher
    tID = teacher.id
    cursor = connection.cursor()
    args = [tID]
    cursor.callproc('classList', args)
    results = cursor.fetchall();
    cursor.close()
    context = {'results': results}

    return render(request, 'createQuiz/classes.html', context)


def generate_random_string(length=6):
    # Generate a random string of defined 'length' with a combination of letters and numbers
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def createClassPage(request):
    form = ClassListForm()
    random_string = generate_random_string()
    msg = ""
    if request.method == 'POST':
        form = ClassListForm(request.POST)
        if form.is_valid():
            teacher = request.user.teacher
            tID = teacher.id
            cname = request.POST['className']
            sbjct = request.POST['subject']
            sctn = request.POST['section']
            eKey = request.POST['enrollKey']
            result = ""
            cursor = connection.cursor()
            args = [cname, sbjct, sctn, eKey, tID, result]
            cursor.callproc('createClass', args)
            result = cursor.fetchall()
            msg = result[0][0]
            cursor.close()
        else:
            print("error in form")

    context = {'form': form, 'msg': msg, 'random_string': random_string}
    return render(request, 'createQuiz/createClass.html', context)


def classInfo(request, id):
    classData = ClassList.objects.get(classID=id)
    msg = ""
    form = AddTopic()
    cID = classData.classID
    cursor = connection.cursor()
    args = [cID]
    cursor.callproc('topicList', args)
    results = cursor.fetchall();
    cursor.close()

    if request.method == 'POST':
        form = AddTopic(request.POST)
        if form.is_valid():
            tName = request.POST['topic']
            description = request.POST['description']
            result = ""
            cursor = connection.cursor()
            args = [tName, description, cID, result]
            cursor.callproc('createTopic', args)
            result = cursor.fetchall()
            msg = result[0][0]
            cursor.close()
            return redirect('classInfo', cID)

        else:
            print("error")
    context = {'classData': classData, 'form': form, 'msg': msg, 'results': results}
    return render(request, 'createQuiz/classInfo.html', context)


def topicInfo(request, id):
    topicData = TopicList.objects.get(topicID=id)
    cID = topicData.classID_id
    classData = ClassList.objects.get(classID=cID)
    tID = topicData.topicID
    msg = ""
    form = AddQuiz()

    cursor = connection.cursor()
    args = [tID]
    cursor.callproc('quizList', args)
    results = cursor.fetchall();
    cursor.close()

    if request.method == 'POST':
        form = AddQuiz(request.POST)
        if form.is_valid():
            qName = request.POST['quiz']
            description = request.POST['description']
            result = ""
            cursor = connection.cursor()
            args = [qName, description, tID, result]
            cursor.callproc('createQuiz', args)
            result = cursor.fetchall()
            msg = result[0][0]
            cursor.close()
            return redirect('topicInfo', tID)
        else:
            print("error")

    context = {'topicData': topicData, 'classData': classData, 'msg': msg, 'form': form, 'results': results}
    return render(request, 'createQuiz/topicInfo.html', context)


def quizSet(request, id):
    quizData = QuizList.objects.get(quizID=id)
    tID = quizData.topicID_id
    topicData = TopicList.objects.get(topicID=tID)
    cID = topicData.classID_id
    qID = quizData.quizID
    classData = ClassList.objects.get(classID=cID)
    msg = ""
    form = AddQuestion()

    cursor = connection.cursor()
    args = [qID]
    cursor.callproc('questionList', args)
    results = cursor.fetchall();
    cursor.close()

    if request.method == 'POST':
        form = AddQuestion(request.POST)
        if form.is_valid():
            question = request.POST['question']
            description = request.POST['description']
            cA = request.POST['cA']
            cB = request.POST['cB']
            cC = request.POST['cC']
            cD = request.POST['cD']
            answer = request.POST['answer']
            result = ""
            cursor = connection.cursor()
            args = [question, description, cA, cB, cC, cD, answer, qID, result]
            cursor.callproc('createQuestion', args)
            result = cursor.fetchall()
            msg = result[0][0]
            cursor.close()
            return redirect('quizSet', qID)
        else:
            print("error")

    context = {'classData': classData, 'quizData': quizData, 'topicData': topicData, 'msg': msg, 'form': form, 'results': results}
    return render(request, 'createQuiz/quizSet.html', context)


def deleteQuestion(request, id):
    questionData = QuestionSet.objects.get(questionID=id)
    qID = questionData.quizID_id
    quizData = QuizList.objects.get(quizID=qID)
    result = ""
    if request.method == 'POST':
        cursor = connection.cursor()
        args = [questionData.questionID, result]
        cursor.callproc('deleteQuestion', args)
        result = cursor.fetchall();

        cursor.close()
        return redirect('/quizSet/%s' % qID)

    context = {'item': questionData, 'quiz': quizData, 'result': result}
    return render(request, 'createQuiz/deleteQuestion.html/', context)


def updateQuestion(request, id):
    questionData = QuestionSet.objects.get(questionID=id)
    qID = questionData.quizID_id
    quizData = QuizList.objects.get(quizID=qID)
    msg = ""
    questionID = questionData.questionID
    if request.method == 'POST':
        question = request.POST['question']
        description = request.POST['description']
        cA = request.POST['cA']
        cB = request.POST['cB']
        cC = request.POST['cC']
        cD = request.POST['cD']
        answer = request.POST['answer']
        result = ""
        cursor = connection.cursor()
        args = [question, description, cA, cB, cC, cD, answer, questionID, result]
        cursor.callproc('updateQuestion', args)
        result = cursor.fetchall()
        msg = result[0][0]
        cursor.close()
        if msg == 1:
            messages.success(request, 'Question updated successfully')
        elif msg == 0:
            messages.info(request, 'No changes applied')
        return redirect('/quizSet/%s' % qID)

    context = {'item': questionData, 'quiz': quizData, 'msg': msg}
    return render(request, 'createQuiz/updateQuestion.html/', context)


def updateClass(request, id):
    classData = ClassList.objects.get(classID=id)
    cID = classData.classID
    msg = ""
    if request.method == 'POST':
        cName = request.POST['className']
        sbjct = request.POST['subject']
        sction = request.POST['section']
        enKey = request.POST['enrollKey']
        result = ""
        cursor = connection.cursor()
        args = [cName, sbjct, sction, enKey, cID, result]
        cursor.callproc('updateClass', args)
        result = cursor.fetchall()
        msg = result[0][0]
        cursor.close()
        if msg == 1:
            messages.success(request, 'Class updated successfully')
        elif msg == 0:
            messages.info(request, 'No changes applied')
        return redirect('/classInfo/%s' % cID)

    context = {'classData': classData, 'msg': msg}
    return render(request, 'createQuiz/updateClass.html', context)



def updateTopic(request, id):
    topicData = TopicList.objects.get(topicID=id)
    tID = topicData.topicID
    msg = ""
    if request.method == 'POST':
        tName = request.POST['tName']
        tDescription = request.POST['tDescription']
        result = ""
        cursor = connection.cursor()
        args = [tName, tDescription, tID, result]
        cursor.callproc('updateTopic', args)
        result = cursor.fetchall()
        msg = result[0][0]
        cursor.close()
        if msg == 1:
            messages.success(request, 'Topic updated successfully')
        elif msg == 0:
            messages.info(request, 'No changes applied')
        return redirect('/topicInfo/%s' % tID)

    context = { 'topicData': topicData}
    return render(request, 'createQuiz/updateTopic.html', context)
