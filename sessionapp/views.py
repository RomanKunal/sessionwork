from django.shortcuts import render

# Create your views here.

# def index(request):
#     request.session['name'] = 'John'
#     request.session['age'] = 20
#     return render(request, 'index.html')

# def get(request):
#     name = request.session.get('name')
#     age = request.session.get('age')
#     keys=request.session.keys()
#     items=request.session.items()
#     return render(request, 'get.html', {'name': name, 'age': age, 'keys': keys, 'items': items})

# def clear(request):
#     if 'name' in request.session:
#         del request.session['name']
#     return render(request, 'clear.html')

# def flush(request):
#     request.session.flush()
#     return render(request, 'flush.html')


def index(request):
    res=render(request,'index.html')
    res.set_cookie('name','Kunal')
    res.set_cookie('age','20')
    return res

def get(request):
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    keys=request.COOKIES.keys()
    items=request.COOKIES.items()
    return render(request,'get.html',{'name':name,'age':age,'keys':keys,'items':items})

def clear(request):
    res=render(request,'clear.html')
    res.delete_cookie('name')
    res.delete_cookie('age')
    return res

def flush(request):
    res=render(request,'flush.html')
    res.delete_cookie('name')
    res.delete_cookie('age')
    return res





