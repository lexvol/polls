from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Question, Choice, Subcategory
from .services import reset


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
    # if not request.session['result']['poll_name']:
    #     request.session['result'] = {'poll_name': Question.}
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
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'balanceWheel/details.html', {
                      'question': question,
                      'error_message': 'Вы не выбрали не один из вариантов ответа.'},
                      )
    else:
        subcategory_name = Subcategory.objects.get(id=choice.question.subcategory_id).subcategory_name
        points = request.session.get('result', {}).get(f'{subcategory_name}', 0) + choice.points
        request.session['result'] |= {subcategory_name: points}
        last_question = Question.objects.last()
        if question_id != last_question.id:
            question = Question.objects.get(pk=choice.link_id or question_id + 1)
            return render(request, 'balanceWheel/details.html', {'question': question,
                                                                 'test': request.session.get('result')})
        response = render(request, 'balanceWheel/results.html', {'data': request.session.get('result')})
        return response
