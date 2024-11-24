from django.shortcuts import render, get_object_or_404, redirect
from .models import Page

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    if page_slug != page.slug:
        return redirect(page, permanent=True)
    return render(request, 'pages/sample.html', {'page': page})

