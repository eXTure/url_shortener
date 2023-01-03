import secrets
from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Url


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
    expired_message = ""
    url = Url.objects.get(short_url=short_url)
    original_url = url.full_url
    expiration_date = url.date_created + timedelta(days=7)
    if timezone.now() > expiration_date:
        url.is_active = False
        url.save()
        expired_message = "Your short URL is expired"
    if url.clicks > 3:
        url.is_active = False
        url.save()
        expired_message = "You've reached the maximum number of clicks for this short URL"
    url.clicks += 1
    url.save()
    if "http" not in original_url:
        original_url = f"https://{original_url}"
    if url.is_active:
        return redirect(original_url)
    else:
        return render(request, "url_expired.html", {"base": "base.html", "message": expired_message})
