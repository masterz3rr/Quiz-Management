from django.shortcuts import render


# Create your views here.
def quizPage(request):
    context = {}
    return render(request, 'createQuiz/quizzes.html', context)
