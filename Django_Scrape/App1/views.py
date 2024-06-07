from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import pandas as pd
from .models import Geonode
from .tasks import My_Work

class m1(APIView):

    def post(self, request):

        My_Work.delay()
        
        return Response(data={"msg":"ok"})

        # urls = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"

        # response = requests.get(urls)

        # data = response.json()

        # if data:

        #     data_set = data['data']

        #     # print(data_set)

        #     # Scrape_data = pd.DataFrame()
            
        #     for i in data_set:

        #         ip_address = i.get('ip', None)

        #         # print(ip_address)
        #         port = i.get('port', None)
        #         protocols = i.get('protocols', None)
        #         country = i.get('country', None)
        #         uptime = i.get('upTime', None)

        #         Geonode.objects.create(ip_address=ip_address,port=port,protocal=protocols,country=country,Uptime=uptime)

        #         # Scrape_data = Scrape_data._append({'ip_address': ip_address,
        #         #                       'port': port,
        #         #                       'protocols': protocols,
        #         #                       'country': country,
        #         #                       'uptime': uptime}, ignore_index=True)
                
        #     return Response(data={"save Successfully"})

        # else:
        # return Response(data= {"msg": "failed to retrieve data from the API"})
