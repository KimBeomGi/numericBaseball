from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

def soloPlay1(request):
    if request.method == "GET":
        return render(request, 'soloPlay1.html')

def soloPlay2(request):
    if request.method == "GET":
        return render(request, 'soloPlay2.html')
    elif request.method == "POST":
        selected_numbers = request.POST.get('selectedNumbers')
        
        print(selected_numbers)
        context = {
            "posts" : '포스트방식',
            "selectedNumbers": selected_numbers,
        }
        return render(request, 'soloPlay2.html', context)


def multiPlay1(request):
    if request.method == "GET":
        return render(request, 'multiPlay1.html')

def multiPlay2(request):
    if request.method == "GET":
        return render(request, 'multiPlay2.html')

def test(request):
    if request.method == "GET":
        return render(request, 'test.html')


def about(request):
    if request.method == "GET":
        return render(request, 'about.html')

def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')