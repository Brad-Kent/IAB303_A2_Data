import urllib.request
url = 'https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=a34d4b5f-8e3c-4995-8950-2e84fd7bb4d5'  
fileobj = urllib.request.urlopen(url)
print(fileobj.read())