import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_backend.settings')
django.setup()

from django.test import Client

c = Client()
urls = ['/', '/admission/', '/faculty/', '/admin/']
for url in urls:
    response = c.get(url)
    print(f"GET {url} : {response.status_code}")
