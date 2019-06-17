from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#比较灵活
#     return HttpResponse('hello')

def home(request):
    return render(request,'home.html')

def count(request):
    text=request.GET['text']
    print(request.GET['text'])
    #词频统计
    result={}
    for i in text:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    print(result)
    result=sorted(result.items(),key=lambda x:x[1],reverse=True)

    #返回到另一个页面
    return render(request,'count.html',{'count_result':result})

def about(request):
    return render(request,'about.html')