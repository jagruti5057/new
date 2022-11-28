from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    return render(request,'index.html')
# def index(request):
#     return HttpResponse("hello this is home page "'''<a href="http://127.0.0.1:8000/about/">'''"click </a>")
def about(request):
    return HttpResponse("this is about page""<a href=http://127.0.0.1:8000/>"" back </a>" 'or go to'
    "<a href=http://127.0.0.1:8000/contact/> next page</a>")
def contact(request):
    return HttpResponse("hello this is contact page "'''<a href="http://127.0.0.1:8000/">'''"click </a>")

def removepage(request):
    # text1=request.GET.get('text','default')
    # print(text1)
    # return HttpResponse("done your text will be securly save")
     return HttpResponse("")


def analyize(request):
    text1=request.GET.get('text','default')
    removepage=request.GET.get('removepage','off')
    print(removepage )
    print(text1)
    if removepage == "on":
        punctuations='!()-[]{}:;''"/\.<>?*#@$%^&*_~'
        analyize=''
        for char in text1:
            if char not in punctuations:
                analyize=analyize + char
        analyize=text1
        params={{'purpose':'remove page','analyzed_text':analyize}}
        return render(request ,"analyze.html",params)
    else:
        return HttpResponse("error")