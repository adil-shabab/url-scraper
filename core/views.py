from bs4 import BeautifulSoup
from django.shortcuts import redirect, render
import requests
from .models import Website, Favourite

# Create your views here.
def home(request):
    fav_count = Favourite.objects.all().count()
    history_count = Website.objects.all().count()
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
        
        # ********************* images *************************
        images = soup.find_all('img')
        image_links = []

        for image in images:
            image_link = link+image['src']
            image_links.append(image_link)



        # *********************** vedio ********************
        # videos = soup.find_all('source')
        # videos_links = []
        # for video in videos:
        #     video_link = link+video['src']
        #     videos_links.append(video_link)
         
        # videos = soup.find_all('video')
        # videos_links = []
        # for video in videos:
        #     video_link = link+video['src']
        #     videos_links.append(video_link)
         
        web = Website(domain=link, word_count=word_count, urls=urls_links, images=image_links)
        web.save()
        fav_count = Favourite.objects.all().count()
        history_count = Website.objects.all().count()

        
        context= {
            'website': web,
            'link': link,
            'word_count' : word_count,
            'urls': urls_links,
            'images': image_links,
            'fav_count' : fav_count,
            'history_count' : history_count
        }

        return render(request, 'index.html', context)

    context={
        'fav_count' : fav_count,
        'history_count' : history_count
    }



    return render(request, 'index.html', context)




def singleImages(request, pk):
    fav_count = Favourite.objects.all().count()
    history_count = Website.objects.all().count()
    website = Website.objects.get(id=pk)
    all_img = website.images.replace('[','')
    all_imgs = all_img.replace(']','')
    images = all_imgs.split()
    all_images = []
    for x in images:
        img = x.replace("'","").replace(",","")
        all_images.append(img)


    # print(images)
    context = {
        'website': website,
        'images': all_images,
        'fav_count' : fav_count,
        'history_count' : history_count
    }

    return render(request, 'images.html', context)
    

def singleUrl(request, pk):
    fav_count = Favourite.objects.all().count()
    history_count = Website.objects.all().count()
    website = Website.objects.get(id=pk)
    all_url = website.urls.replace('[','')
    all_urls = all_url.replace(']','')
    urls = all_urls.split()
    all_urls = []
    for x in urls:
        img = x.replace("'","").replace(",","")
        all_urls.append(img)

    context = {
        'website': website,
        'urls': all_urls,
        'fav_count' : fav_count,
        'history_count' : history_count
    }

    return render(request, 'url.html', context)



def history(request):

    all_websites = Website.objects.all()
    fav_count = Favourite.objects.all().count()
    history_count = Website.objects.all().count()
    context = {
        'websites' : all_websites,
        'fav_count' : fav_count,
        'history_count' : history_count
    }


    return render(request, 'history.html', context)



def fav(request):
    all_websites = Favourite.objects.all()
    fav_count = Favourite.objects.all().count()
    history_count = Website.objects.all().count()
    context = {
        'websites' : all_websites,
        'fav_count' : fav_count,
        'history_count' : history_count
    }
    return render(request, 'fav.html', context)


def addtofav(request,pk):
    website = Website.objects.get(id=pk)

    fav = Favourite(website=website)
    if Favourite.objects.filter(website=website):
        pass
    else:
        fav.save()
    
    return redirect('history')




def removefav(request, pk):
    fav = Favourite.objects.get(id = pk)
    fav.delete()

    return redirect('fav')