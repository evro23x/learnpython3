# import json
# import urllib
# # import urllib.request
#
# url = "http://api.data.mos.ru/v1/datasets/2009/rows"
# response = urllib.urlopen(url)
# data = json.loads(response.read())
# print(data)

import json
import urllib


data = urllib.urlopen("http://api.data.mos.ru/v1/datasets/2009/rows").read()
output = json.loads(data)
print(output)
# print(data)
#