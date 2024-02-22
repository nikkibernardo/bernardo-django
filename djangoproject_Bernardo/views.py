from django.shortcuts import render
from django.http import HttpResponse

def inder(request):
    return HttpResponse('Hello, World!')

def mission(request):
    message = '<h1>CCMS Mission</h1> <br> <h2>The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence. </h2>'
    return HttpResponse(message)

def vision(request):
    
    message = '<h1>CCMS Vision</h1> <br> <h2> The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.</h2>'
    return HttpResponse(message)

def objectives(request):
    
    message = '<h1>CCMS Objectives</h1> <br> <h2> HELLO CCMS</h2>'
    return HttpResponse(message)