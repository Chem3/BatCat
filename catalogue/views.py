from django.shortcuts import render, get_object_or_404
from .models import Sample, Method
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.db.models import Q


# Create your views here.
def list_objects(request):
    sample_list = Sample.objects.order_by('-amount')[:5]
    labels = []
    data = []
    for sample in sample_list:
        labels.append(sample.name)
        data.append(sample.amount)

    return render(request, 'catalogue/list.html', {'samples': sample_list,
                                                   'data': data, 'labels': labels
                                                   })


def detail(request, pk):
    sample_detail = get_object_or_404(Sample, pk=pk)
    return render(request, 'catalogue/detail.html', {'sample': sample_detail })


class SearchResultsView(ListView):
    model = Sample
    template_name = 'catalogue/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Sample.objects.filter(
            Q(name__icontains=query) |
            Q(barcode__icontains=query)
        )
        return object_list

