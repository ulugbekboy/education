from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render
from ..university.models import *
from ..students.models import *
# from ..contact.models import Contact
# Create your views here.
from ..news.models import *
from .models import *
from django.core.serializers import serialize
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max,Min

def error_404_view(request,exception):
    return render(request, 'others/404.html')


def filter_data(request):

    countrys =request.GET.getlist('country[]')
    study =request.GET.getlist('study[]')
    faculty =request.GET.getlist('faculty[]')
    allProducts = University.objects.all()
    if len(countrys)>0:
        allProducts=allProducts.filter(country__name__in =countrys).distinct()


    if len(study)>0:
        allProducts=allProducts.filter(study_form__name__in=study).distinct()



    if len(faculty)>0:
        allProducts=allProducts.filter(faculty__name__in=faculty).distinct()

    t = render_to_string('blog/ajax/univers.html',{'univer':allProducts})
    return JsonResponse({'univer':t})



def index(request):
    top_university = University.objects.filter(top_universities =True)
    students = Gallery.objects.all()
    university = University.objects.all().count()
    countries =Country.objects.filter(banner=True)
    country = countries.count()

    testimonials = Testimonials.objects.all()
    faq = FAQ.objects.all()


    advantage = Advantage.objects.all()


    context = {

        'students': students,
        'faq':faq,

        'advantage': advantage,
        'top_university':top_university,
        'university':university,
        'country':country,
        'countries':countries,
        'testimonials':testimonials

    }
    return render(request, 'base/index.html',context)


def error(request):
    context = {

    }
    return render(request, 'others/404.html', context)


def page(request):
    context = {

    }
    return render(request, 'others/cons.html', context)





def loadding(request,*args,**kwargs):
    upper =kwargs.get('num_posts')
    lower =upper -3
    news = list(News.objects.values()[lower:upper])
    news_size =len(News.objects.all())
    size =True if upper>=news_size else False
    return JsonResponse({'news':news,'max':size}, safe=False)



def load_students(request,*args,**kwargs):
    upper = kwargs.get('num_posts')
    lower = upper - 3
    univer = list(University.objects.values()[lower:upper])
    univer_size = len(Students.objects.all())
    slize = True if upper >= univer_size else False
    return JsonResponse({'max': slize, 'univer': univer}, safe=False)




def search(request):
    if request.method == 'GET':
        search_text = request.GET.get('search_text')

    else:
        search_text = ''


    univer =University.objects.filter(name__contains=search_text)
    if univer.count() > 5:
        active = True

    t = render_to_string('blog/search.html', {'univer': univer,'search_text':search_text})

    return JsonResponse({'data': t})


def filter_univer(request):

    countrys =request.GET.getlist('country[]')
    print(countrys)
    study =request.GET.getlist('study[]')
    print(study)
    faculty =request.GET.getlist('faculty[]')
    print(faculty)
    allProducts = University.objects.all()
    if len(countrys)>0:
        allProducts=allProducts.filter(country__name__in =countrys).distinct()
    if len(study)>0:
        allProducts=allProducts.filter(study_form__name__in=study).distinct()



    if len(faculty)>0:
        allProducts=allProducts.filter(faculty__name__in=faculty).distinct()

    t = render_to_string('blog/ajax/univers.html',{'univer':allProducts})
    return JsonResponse({'univer':t})





def search_univer(request):
    if request.method == 'GET':
        search_text = request.GET.get('search_text')
    else:
        search_text = ''

    univer = University.objects.filter(country__name='USA')
    univer = univer.filter(name__contains =search_text)
    print(univer)
    # univer = University.objects.filter(name__contains=search_text)
    if univer.count() > 5:
        active = True

    t = render_to_string('blog/search.html', {'univer': univer, 'search_text': search_text})

    return JsonResponse({'data': t})