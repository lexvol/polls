from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Question, Choice
from .services import get_overall_result


# generic views
class IndexView(generic.ListView):
    template_name = 'balanceWheel/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('id')[:15]


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     return render(request, 'balanceWheel/index.html', {'latest_question_list': latest_question_list})


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
        return render(request, 'balanceWheel/vote.html', {
            'question': question,
            'error_message': 'Вы не выбрали не один из вариантов ответа.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('wheel:results', args=question_id))
