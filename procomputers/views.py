from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "index.html"
    extra_context = {"title" : "ProComputers"}

class contacts(TemplateView):
    template_name = "contacts.html"
    extra_context = {"title" : "Contacto"}

class empleados(TemplateView):
    template_name = "empleados.html"
    extra_context = {"title" : "Empleados"}

class servicios(TemplateView):
    template_name = "servicios.html"
    extra_context = {"title" : "Servicios"}


