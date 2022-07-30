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
        soup_code = BeautifulSoup(source_code, 'html.parser')
        print(soup_code)
        for each_text in soup_code.findAll('div'):
            content = each_text.text
            print(content)
            word_count += len(content)




        # *********************** urls **********************
        urls = soup.find_all('a')
        urls_links = []

        for url in urls:
            href = url['href']

            if href.startswith('#'):
                pass
            elif href.startswith('/'):
                updated_href = link+href
                urls_links.append(updated_href)
            elif href.startswith('http'):
                urls_links.append(href)
            else:
                pass





        # ******************* media **************************
        images = soup.find_all('img')
        image_links = []

        for image in images:
            image_link = link+image['src']
            image_links.append(image_link)






        context= {
            'word_count' : word_count,
            'urls': urls_links,
            'images': image_links
        }

        return render(request, 'index.html', context)





    return render(request, 'index.html')