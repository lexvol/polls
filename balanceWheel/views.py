from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Question, Choice
from .services import get_overall_result, reset


# generic views
# class IndexView(generic.ListView):
#     template_name = 'balanceWheel/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.order_by('id')[:15]


def index(request):
    param = request.GET.get("param")
    if param == 'restart':
        reset()
    latest_question_list = Question.objects.order_by('id')[:15]
    return render(request, 'balanceWheel/index.html', {'latest_question_list': latest_question_list})


def details(request: HttpRequest, question_id: int) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Вопрос не существует')
    return render(request, 'balanceWheel/details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'balanceWheel/results.html', {'question': question})


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'balanceWheel/details.html', {
                      'question': question,
                      'error_message': 'Вы не выбрали не один из вариантов ответа.'},
                      )
    else:
        if question_id != len(Question.objects.all()):
            selected_choice.vote = True
            selected_choice.save()
            question = Question.objects.get(pk=question_id + 1)
            return render(request, 'balanceWheel/details.html', {'question': question})

        response = render(request, 'balanceWheel/results.html', {'data': get_overall_result()})
        return response
