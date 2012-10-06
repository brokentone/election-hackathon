from django.template import Context, loader
from issue_engine.models import Statement 
from django.http import HttpResponse

def home(request):
    list_questions = Statement.objects.all()[:5]
    t = loader.get_template('index.html')
    c = Context({
        'list_questions ': list_questions,
    })
    return HttpResponse(t.render(c))
