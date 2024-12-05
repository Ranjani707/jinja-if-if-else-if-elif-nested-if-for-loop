from django.shortcuts import render

# Create your views here.

def conditional(request):
    d={'name':'ranju','age':22,'gender':'female','mobile':'9361706895','nationality':'indian'}
    return render(request,'conditional.html',context=d)
