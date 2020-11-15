from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Page, PageConnector


# Create your views here.
class TestView(TemplateView):

    template_name = "test_view.html"

    def get_context_data(self, **kwargs):

        pages = Page.objects.all()
        page_ids = []
        for page in pages:
            page_ids.append(page.id)

        connectors = PageConnector.objects.filter(page__in=page_ids)

        context = super().get_context_data(**kwargs)
        context['pages'] = pages
        context['connectors'] = connectors
        return context
