import matplotlib.pyplot
import urllib, urllib2

response = urllib2.urlopen('http://demo.ckan.org/api/3/action/group_list', data_string)
assert response.code == 200

response_dict = json.loads(response.read())

assert response_dict['success'] is True
result = response_dict['result']

print(result)
