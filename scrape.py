import urllib.request
import re

url = "https://www.movitel.co.mz/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    imgs = re.findall(r'<img[^>]+src="([^">]+)"', html)
    for img in imgs:
        if 'mola' in img.lower() or 'logo' in img.lower():
            print(img)
except Exception as e:
    print("Error:", e)
