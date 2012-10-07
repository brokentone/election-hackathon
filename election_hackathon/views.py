from django.template import Context, loader
from issue_engine.models import Statement 
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    list_questions = Statement.objects.all()[:5]
    t = loader.get_template('index.html')
    c = Context({
        'list_questions ': list_questions,
    })
    return HttpResponse(t.render(c))

def indextest(request):
    issues = ['Economy', 'Govt Spending', 'Energy']
    statements = ['Mitt said', 'Obama said']
    return render_to_response('templates/index.html',
        {"issues": issues},
        {"statements": statements}, context_instance=RequestContext(request))
