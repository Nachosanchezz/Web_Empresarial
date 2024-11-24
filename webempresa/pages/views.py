from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request, page_id, slug):
    # Intentar obtener la página con el ID y slug proporcionados
    page = get_object_or_404(Page, id=page_id, slug=slug)

    # Renderizar la plantilla si la página existe
    return render(request, 'pages/sample.html', {'page': page})



