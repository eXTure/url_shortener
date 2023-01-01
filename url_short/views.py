import secrets

from django.shortcuts import render, redirect

from .models import Url, Clicks


def index(request):
    return render(request, "index.html", {"base": "base.html"})


def url_result(request):
    if request.method == "POST":
        url = request.POST.get("url")
        unique_id = secrets.token_hex(8)
        short_url = f"localhost:8000/{unique_id}"
        new_url = Url(full_url=url, short_url=unique_id)
        new_url.save()
        return render(request, "url_result.html", {"base": "base.html", "short_url": short_url, "url": url})


def redirect_view(request, short_url):
    url = Url.objects.get(short_url=short_url)
    original_url = url.full_url
    if "http" not in original_url:
        original_url = f"https://{original_url}"
    url.clicks_set.create()
    return redirect(original_url)
