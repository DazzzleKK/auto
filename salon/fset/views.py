from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.forms.models import inlineformset_factory

from .models import Sale, Auto, Specs

from nested_formset import nestedformset_factory

# Create your views here.


class AutoList(ListView):
    model = Sale
    fields = "__all__"


class CreateSale(CreateView):
    model = Sale
    fields = ["name"]

    def get_success_url(self):
        return reverse("list")


class EditAutoView(UpdateView):
    model = Sale
    fields = "__all__"
    template_name = "fset/specs_form.html"

    def get_form_class(self):
        return nestedformset_factory(
            Sale,
            Auto,
            nested_formset=inlineformset_factory(
                Auto, 
                Specs, 
                fields="__all__"
            )
        )

    def get_success_url(self):
        return reverse("list")
