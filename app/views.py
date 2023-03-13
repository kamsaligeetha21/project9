from django.shortcuts import render

# Create your views here.


def jinja_print(request):
    d={'name':'CINNU','age':5}
    return  render(request,'jinja_print.html',context=d)
