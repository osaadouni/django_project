from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.db.models import F
from django.views import generic 

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]  # -pub_date => ORDER BY pub_date DESC 


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
   model = Question
   template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # use F() expression to update the votes 
    # avoid race conditions ( when 2 threads try to update at the same time ) 
    try: 
        question.choice_set.filter(pk=request.POST['choice']).update(votes=F('votes') + 1)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question, 
            'error_message': "Oops! You didn't select a choice.", 
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing  
        # with POST data. This prevents data from being posted twice if 
        # a user hits the Back button.
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
        
