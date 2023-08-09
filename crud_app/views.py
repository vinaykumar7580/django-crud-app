from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

data = {
    "name": "Ram",
    "age": 20,
    "city": "Delhi"
}

def create(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        data[key] = value
    return render(request, "create.html")

def read(request):
    return render(request, "read.html", {"data": data})

def update(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        if key in data:
            data[key] = value
    return render(request, "update.html")

def delete(request):
    if request.method == "POST":
        key = request.POST.get("key")
        if key in data:
            del data[key]
    return render(request, "delete.html")
