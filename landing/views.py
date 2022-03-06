from django.shortcuts import render

from landing.models import basicinfo, questions, res


def home(request):
    #sweetify.success(request, 'You did it', text='Your Form has been Updated',persistent='Hell yeah')
    return render(request,'index.html')
   

def result(request):
    return render(request,'result.html')

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        hobby=request.POST['hobby']
        basicinfo(name=name,timepass=hobby).save()
        return render(request,'form.html',{'context':'true'})
    else:
        return render(request,'form.html')
def question(request):
    return render(request,'Ques.html')


def quiz(request,qid):
    
    if qid == 7:
        return render(request,'result.html')
    ob1=questions.objects.get(qid=qid)
    if request.method == 'POST':
        ans=request.POST['q1']
        res(responce=ans).save()
        return render(request,'Ques.html',{'context':ob1,'next':qid+1,})
    else:
         return render(request,'Ques.html',{'context':ob1,'next':qid+1})


