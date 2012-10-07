from django.template import RequestContext, Context, loader
from issue_engine.models import Statement 
from django.http import HttpResponse
from django.shortcuts import render_to_response
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

def home(request):
    list_questions = Statement.objects.all()[:5]
    t = loader.get_template('index.html')
    c = Context({
        'list_questions ': list_questions,
    })
    return HttpResponse(t.render(c))

def indextest(request):
    issue_list_request = urllib2.urlopen("http://api.washingtonpost.com/politics/transcripts/api/v1/issue/?key=484BBEB2-D0B8-461A-8A3F-1B213DE9797B").read()
    issue_list_json = json.loads(issue_list_request)
    issues = []
    for i in issue_list_json['objects']:
        issues.append(i['name'])

    #statement_list_request = urllib2.urlopen("

    statements = ['Mitt said', 'Obama said']
    return render_to_response('index.html',
        {'issues': issues, 'statements':statements,}, context_instance=RequestContext(request))
