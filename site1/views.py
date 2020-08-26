from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from time import sleep
import json
import math
import re
from django.shortcuts import redirect
from django.urls import reverse

import os

from django.http import  HttpResponseNotFound
from django.template.loader import render_to_string

#-----------------------testing---------------------------

#def admin_404(request):
#    return HttpResponseNotFound(render_to_string('wagtailadmin/404.html'))
def admin_404(request, exception=None):
    return HttpResponse('Error handler content', status=404)

#http://localhost:8000/page/?name=codeberry.html
def page(request):
    body = request.GET['name']
    #return render(request, 'site1/page.html', {'body':body})
    return HttpResponse(name)

#----------------------------------------------------------

def robots(request):
    return HttpResponseRedirect("/static/site1/robots.txt")

def about(request):
    return render(request, 'site1/about.html', {})

def answer_me(request):
    method = request.method

    if(method == "GET"):
        question = request.GET['question']
        return HttpResponse("Your question was: '" + question+"'")

    if(method == "POST"):
        pass
        question = request.POST['question']
        return HttpResponse("Your question was: '" + question+"'")

    return HttpResponse("hello!")

def reply(request):
    req = request.read()
    print(req)
    if('timeout' in request.GET):
        timeout = int(request.GET['timeout'])
        sleep(timeout)
        return HttpResponse("here I am!")
    if('json' in request.POST):
        name = request.POST['name']
        #string
        jsonStr = request.POST['json']
        #dictionary
        jsonDict = json.loads(jsonStr)
        return HttpResponse("Your request was: " + str(req))
    if request.FILES:
        comment = request.POST['comment']
        file = request.FILES['fileToUpload']
        #print file.size
        msg = "Your request was: comment=" + comment + "  file=" + file.name  #+ " file size=" + file.size
        return HttpResponse(msg)
    #catch all response, just in case
    return HttpResponse("hello!")

def reply2(request):
    data = {}
    data['key1'] = "a"
    data['key2'] = 10
    data = json.dumps(data)
    return HttpResponse(data)

def answer_me2(request):

    if('arg' in request.GET):
        arg = request.GET['arg']
        if(arg == "1"):
            return HttpResponse("response nr 1")
        if(arg == "2"):
            return HttpResponse("response nr 2")

    return HttpResponse("hello!")

def send_data(request):
    jsonStr = request.body

    myDictionary = json.loads(jsonStr)

    proposition = myDictionary['proposition']
    number = myDictionary['number']
    proposition = proposition.lower()
    number = math.pi
    myDictionary['proposition'] = proposition
    myDictionary['number'] = number

    jsonStr = json.dumps(myDictionary)

    return HttpResponse(jsonStr)

def redirect_response(request):
    #if(request.method == "POST"):
    #    firstname = request.POST['firstname']
    #    lastname = request.POST['lastname']

        return render(request, 'site1/redirect_response.html', {'firstname':firstname,'lastname':lastname})

def reply_form(request):
    print(request.POST)
    if(request.method == "POST"):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        about_file = ''
        if request.FILES:
            file = request.FILES['file']
            about_file =  file.name  + " file size=" + str(file.size) + " bytes"
        return render(request, 'site1/site1_redirect_response.html', {'firstname':firstname,'lastname':lastname, 'about_file':about_file})
        #return redirect(reverse('redirect-response'))
    else:
        pass

def reply3(request):

    data = {}

    form = False
    if(request.method == "POST"):
        if('form' in request.POST):
            form = True
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if request.FILES:
            file = request.FILES['file']
            data['fileName'] = file.name
            data['fileSize'] = str(file.size) + " bytes"

    data['firstname'] = firstname
    data['lastname'] = lastname

    jsonData = json.dumps(data)

    return HttpResponse(jsonData)




def echo(request):

    medium = ""

    if(request.method == "GET"):
        if "medium" in request.GET:
            medium = request.GET['medium']

    if(request.method == "POST"):
        if "medium" in request.POST:
            medium = request.POST['medium']

    if medium == "js":
        endLine = "\r\n"
    else:
        endLine = "<br>"

    httpHeaders = ""
    for key in request.META:
        if key.startswith('HTTP_'):
            # hide csrf from response
            if(key == 'HTTP_COOKIE'):
                cookie = request.META[key]
                match = re.search("csrftoken=(\w*)",cookie)
                csrf = match.group(1)
                cookie = cookie.replace(csrf,"***********************************")
                httpHeaders = httpHeaders + key[5:len(key)] + " : " + cookie + endLine
            else:
                httpHeaders = httpHeaders + key[5:len(key)] + " : " + request.META[key] + endLine

    if(request.method == "GET"):

        firstname = request.GET["firstname"]
        lastname = request.GET["lastname"]
        msg = "GET " + request.path + endLine + httpHeaders + endLine + "firstname = " + firstname + endLine + "lastname = " + lastname


    if(request.method == "POST"):

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        msg = "POST " + request.path + endLine + httpHeaders + endLine + "firstname = " + firstname + endLine + "lastname = " + lastname + endLine + endLine

        if request.FILES:
            try:
                file = request.FILES['file']
            except:
                file = None
            try:
                file0 = request.FILES['file0']
            except:
                file0 = None
            if file:
                msg = msg + "file name: " + file.name + " " + str(file.size) + " bytes" + endLine
                msg = msg + "1st 100 bytes of file: " + endLine + str(file.read(100)) + endLine + endLine
            if file0:
                msg = msg + "file name: " + file0.name + " " + str(file0.size) + " bytes" + endLine
                msg = msg + "1st 100 bytes of file: " + endLine + str(file0.read(100)) + endLine + endLine


    #return HttpResponse(msg)
    return render(request, 'site1/site1_response.html', {'msg':msg})



