from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.db.models import F
from django.views import generic 

from .models import Question, Choice

def index(request):
    total_questions = Question.objects.count()
    #latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    latest_question_list = Question.objects.order_by('-pub_date')[:total_questions] 
    #output = '<br> '.join([q.question_text for q in latest_question_list])
    context = { 
        'latest_question_list': latest_question_list,
        'total_questions': total_questions, 
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) 

def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
        
    # use helper function for loose coupling: get() and raise 404 if the object doesn't exist 
    # get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, 'question_id': question_id })

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    #response = f"You're looking at the results of question {question_id}. f-string works!!!"
    #return HttpResponse(response)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def old_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question, 
            'error_message': "You didn't select a choice.", 
        })
    else:
        #orig:  this can cause race conditions ( 2 threads updating the votes at the same time ) 
        #selected_choice.votes += 1
        #selected_choice.save()

        # to avoid race conditions, use: F() 
        # Does not work - error: selected_choice.update(votes=F('votes') + 1) # error: no 'update' attr
        # question.choice_set.filter(pk=request.POST['choice']).update(votes=F('votes') + 1)
        selected_choice.votes = F('votes') + 1 
        selected_choice.save()
        selected_choice.refresh_from_db()
         
        # Always return an HttpResponseRedirect after successfully dealing  
        # with POST data. This prevents data from being posted twice if 
        # a user hits the Back button.
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
        
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
        
