from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from ..models import Question

def index(request):
    page = request.GET.get('page', '1')  # page
    question_list = Question.objects.order_by('-create_date')
    paignator = Paginator(question_list, 10)  # show page per 10 questions.
    page_obj = paignator.get_page(page)
    context = {'question_list': page_obj, 'end_index': paignator.page_range[-1]}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
