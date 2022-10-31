"""
  Python ile IoThook REST Api Testi

  Kod çalıştırıldığında APIKEY ile doğrulama gerçekleştirilir.
  Cihaz api_key ile ilgili veriler IoThook a post edilir.

  Bu ornek IotHook servisine veri almak/gondermek icin baslangic seviyesinde
  testlerin yapilmasini amaclamaktadir.

  v1 : 20 Eylul 2017
  v2 : 19 Agustos 2019
  v3 : 31 Ekim 2022

  Sahin MERSIN - electrocoder

  Daha fazlasi icin

  http://www.iothook.com
  https://www.mesebilisim.com
  https://mesemekatronik.com
  https://electrocoder.blogspot.com
  https://github.com/meseiot/iotexamples

  sitelerine gidiniz.

  Yayin : http://mesebilisim.com

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

  http://www.apache.org/licenses/
"""

import pprint
import requests

headers = {'Content-type': 'application/json'}

# demo account API_KEY
# https://iothook.com/en/device/data/650/
# 650 - iot_get.py
API_KEY = 'f1403e03949c7f9060a4bdd2'  # read api key
url = 'http://iothook.com/api/device/?api_key=' + API_KEY
url += '&start_date=2022-10-31'
url += '&end_date=2022-11-01'

response = requests.get(url, headers=headers)
pprint.pprint(response.json())
