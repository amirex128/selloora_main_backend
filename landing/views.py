from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_POST

from landing.models import LandingSetting, LandingArticle


def home(request):
    return render(request, 'landing/home.html', {
        'setting': LandingSetting.objects.first(),
    })


def blog(request):
    articles = LandingArticle.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'landing/blog.html', {
        'articles': page_obj,
    })


def details(request, slug):
    article = LandingArticle.objects.get(slug=slug)
    return render(request, 'landing/details.html', {
        'article': article,
    })


def contact(request):
    return render(request, 'landing/contact.html')


@require_POST
def save_contact(request):
    return render(request, 'landing/contact.html')


def pricing(request):
    return render(request, 'landing/pricing.html', {
        'setting': LandingSetting.objects.first(),
    })


def faq(request):
    return render(request, 'landing/faq.html', {
        'setting': LandingSetting.objects.first(),
    })


def page_not_found_view(request, exception):
    return render(request, 'landing/404.html', status=404)
