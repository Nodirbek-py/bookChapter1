from django.shortcuts import render, HttpResponse
def home(request):
    name = request.GET.get('name') or "world"
    return HttpResponse("Hello {}".format(name))

def search(request):
    keyword = request.GET["query"]
    return render(request, "search.html", {"keyword": keyword})