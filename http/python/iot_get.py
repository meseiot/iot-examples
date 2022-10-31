"""
  Python ile IoThook REST Api Testi

  IoThook da her cihazin bir kimlik numarasi APIKEY' i vardir. Bu APIKEY kullanilarak veriler IoThook a post edilir.

  Bu ornek IoThook servisine veri almak/gondermek icin baslangic seviyesinde
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

import json
import pprint
import random
import time

import requests

headers = {'Content-type': 'application/json'}

url = 'http://localhost:8000/api/datas/?last=True'

for i in range(100):
    response = requests.get(url, headers=headers)
    pprint.pprint(response.json())
    time.sleep(5)
