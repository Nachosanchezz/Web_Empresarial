from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí podrías guardar los datos o enviar un correo
            return render(request, "contact/contact.html", {
                "form": ContactForm(),  # Mostrar un formulario limpio después del envío
                "ok": "Su mensaje se ha enviado correctamente, en breve nos pondremos en contacto.",
            })
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})

    