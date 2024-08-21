from django.shortcuts import render

# Create your views here.

def index(request):
    request.session['name'] = 'John'
    request.session['age'] = 20
    return render(request, 'index.html')

def get(request):
    name = request.session.get('name')
    age = request.session.get('age')
    keys=request.session.keys()
    items=request.session.items()
    return render(request, 'get.html', {'name': name, 'age': age, 'keys': keys, 'items': items})

def clear(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'clear.html')

def flush(request):
    request.session.flush()
    return render(request, 'flush.html')


