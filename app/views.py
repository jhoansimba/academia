from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import CreateView,ListView, UpdateView, View

# Create your views here.
class SaleInvoicePdf ():
    def get(self, request, *args, **kwargs):
        return HttpResponse ('Hello, world')
