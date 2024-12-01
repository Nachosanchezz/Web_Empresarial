# Web_Empresarial

# **Entrega Proyecto Web Empresarial**

Este proyecto consiste en el desarrollo de una página web para una empresa utilizando el framework **Django**. El proyecto está compuesto por varias aplicaciones, cada una con una funcionalidad específica:

- **Core**: para gestionar las páginas estáticas (portada, historia y visítanos).
- **Services**: para gestionar los servicios que ofrece la empresa.
- **Blog**: para gestionar las entradas y sus categorías.
- **Social**: para manejar los enlaces a las redes sociales en el pie de página.
- **Pages**: para gestionar las páginas secundarias del pie de página.
- **Contact**: para manejar el formulario de contacto y enviar un email con el mensaje.

---

## **Repositorio**

- Link: https://github.com/Nachosanchezz/Web_Empresarial.git
- Usuario: Nachosanchezz
- Despliegue en Vercel: https://web-empresarial-laxj.vercel.app/
---

## **Estructura del Proyecto**

```bash
.
├── manage.py
├── requirements.txt
├── webempresa/                  # Carpeta principal de configuración del proyecto.
│   ├── webempresa/              # Configuración general del proyecto Django.
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── ...
│   ├── core/                    # Aplicación para la gestión de las páginas estáticas.
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── ...
│   ├── services/                # Aplicación para la gestión de los servicios ofrecidos.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── blog/                    # Aplicación para la gestión del blog y sus categorías.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── social/                  # Aplicación para la gestión de los enlaces a redes sociales.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── pages/                   # Aplicación para la gestión de las páginas secundarias.
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── contact/                 # Aplicación para la gestión del formulario de contacto.
│       ├── forms.py
│       ├── views.py
│       ├── ...
│


