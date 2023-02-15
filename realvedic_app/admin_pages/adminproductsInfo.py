import numpy as np
import pandas as pd
import time
from datetime import datetime as dt
import datetime
import re
from operator import itemgetter 
import os
import random


#-------------------------Django Modules---------------------------------------------
from django.http import Http404, HttpResponse, JsonResponse,FileResponse
from django.shortcuts import render
from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField
from django.db.models import F,Func,Q
from django.db.models import Value as V
from django.db.models.functions import Concat,Cast,Substr
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Min, Max
from django.db.models import Subquery
#----------------------------restAPI--------------------------------------------------
from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response

#----------------------------models---------------------------------------------------
from realvedic_app.models import Product_data,categoryy,images_and_banners,blogs,user_cart
#from apiApp.models import user_whishlist,user_data
#from apiApp.models import metal_price,diamond_pricing


#----------------------------extra---------------------------------------------------
import simplejson as json

  
@api_view(['GET'])
def adminProductView(request,format=None):
    status= [{
        "name": "In stock",
        "color": "#00ac69"
        },
        {
        "name": "Out of stock",
        "color": "#FF0000"
        }
  ]
    res={}
    prod_list=[]
    titles=["Product ID", "Product Name", "Category"," HSN", "Stock", "Status","Actions"]

    prod_obj=Product_data.objects.values()
    for i in prod_obj:
        prods={
            'product_id':i['id'],
            'product_name':i["title"],
            "category":i["category"],
            "hsn":i["HSN"],
            "stock": 25,
            "status": "In stock"
        }
        prod_list.append(prods)
    res['titles']=titles
    res['content']=prod_list
    res['status']=status


    

    
    return Response(res)


@api_view(['GET'])
def adminProductView(request,format=None):
    pass

