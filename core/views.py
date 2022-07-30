from bs4 import BeautifulSoup
from django.shortcuts import redirect, render
import requests

# Create your views here.
def home(request):
    if request.method == "POST":
        link = request.POST.get('input')
        r = requests.get(link)
        print(r)
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup)


        # ********************* word count *******************
        word_count = 0
        source_code = requests.get(link).text
        print(source_code)
    return render(request, 'index.html')