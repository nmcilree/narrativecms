from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Page, PageConnector


# Create your views here.
class ChapterView(TemplateView):

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

# Create your views here.
class PageView(TemplateView):

    template_name = "admin/page.html"

def update_position(request):

    # TODO: check that the page belongs to current user

    id = request.GET.get('id', None)
    left = request.GET.get('left', None)
    top = request.GET.get('top', None)

    print(top)
    print(left)

    if id:
        page = Page.objects.get(id=id)
        if page:
            page.top = top
            page.left = left
            page.save()
            return HttpResponse(status=200)
    return HttpResponse(status=500)