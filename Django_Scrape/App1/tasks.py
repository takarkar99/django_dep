from celery import shared_task
from django.contrib.auth import get_user_model
from .models import Geonode
import requests


@shared_task(bind=True)
def My_Work(self):

    urls = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"

    response = requests.get(urls)

    data = response.json()

    if data:

        data_set = data['data']

        # print(data_set)

        # Scrape_data = pd.DataFrame()
        
        for i in data_set:

            ip_address = i.get('ip', None)

            # print(ip_address)
            port = i.get('port', None)
            protocols = i.get('protocols', None)
            country = i.get('country', None)
            uptime = i.get('upTime', None)

            Geonode.objects.create(ip_address=ip_address,port=port,protocal=protocols,country=country,Uptime=uptime)

            # Scrape_data = Scrape_data._append({'ip_address': ip_address,
            #                       'port': port,
            #                       'protocols': protocols,
            #                       'country': country,
            #                       'uptime': uptime}, ignore_index=True)
            
        return "save Successfully"

    else:
        return "failed to retrieve data from the API"
    
