from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    if request.method == "GET":
        input = request.GET.get('input')
        print(input)
    return render(request, 'index.html')