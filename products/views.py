from django.shortcuts import render, HttpResponse
from django.template import loader
import pyrebase
import csv
import os
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


def products(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())


# def products(request):
#     csv_path = staticfiles_storage.path('../static/assets/OpenDataItem.csv')

#     data = []
#     with open(csv_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             data.append(row)

#     # Pass the CSV data to the template context
#     context = {
#         'data': data,
#     }

#     return render(request, 'products.html', context)
