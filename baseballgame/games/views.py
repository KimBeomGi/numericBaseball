import json
import random
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(["GET"])
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

@require_http_methods(["GET"])
def soloPlay1(request):
    if request.method == "GET":
        return render(request, 'soloPlay1.html')


@require_http_methods(["POST"])
def soloPlay2(request):
    # if request.method == "GET":
    #     return render(request, 'soloPlay2.html')
    # elif request.method == "POST":
    if request.method == "POST":
        selected_numbers = request.POST.get('selectedNumbers')
        if selected_numbers == "" or len(selected_numbers) != 3:
            return redirect("soloPlay1")
        selected_numbers_int = []
        for i in range(len(selected_numbers)):
            selected_numbers_int.append(int(selected_numbers[i]))

        
        # 3개의 중복되지 않는 컴퓨터의 베이스볼 넘버 생성
        computer_number = random.sample(range(0,10),3)
        
        context = {
            "selectedNumbers": selected_numbers_int,
            "computerNumber": computer_number
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