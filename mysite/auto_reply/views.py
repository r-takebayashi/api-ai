from django.shortcuts import render
from django.http import HttpResponse
from . import forms

import os.path
import sys, cgi
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


CLIENT_ACCESS_TOKEN = 'f3e4eb1c03b740c7b1bac6d61956f031'


def question_forms(request):
    form = forms.QuestionForm(request.GET or None)


    if form.is_valid():
         message = answer(form.cleaned_data['your_name'])
    else:
         message = 'Please give me question.'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'auto_reply/forms.html', d)

def answer(request):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    question = ai.text_request()
    question.lang = 'ja'  # optional, default value equal 'en'
    question.session_id = '<SESSION ID, UNIQUE FOR EACH USER>'
    form = cgi.FieldStorage()
    
    question.query = request
    response = question.getresponse()
    f = response.read()
    json_dict = json.loads(f)
    return HttpResponse(format(json_dict['result']['fulfillment']['speech']))
#    return HttpResponse(question.query)
