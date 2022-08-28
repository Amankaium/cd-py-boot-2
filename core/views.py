from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serialiers import ProductSerializer
from .models import Product
from .decorators import superuseronly


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@login_required
@superuseronly
def homepage(request):
    return render(request, 'index.html')


class HomeView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        return HttpResponse("Method not allowed", status=405)
