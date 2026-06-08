import urllib.request
import re

url = "https://play.google.com/store/apps/details?id=mz.co.movitel.emola&hl=en"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # find the logo image URL from Google Play
    m = re.search(r'https://play-lh\.googleusercontent\.com/[a-zA-Z0-9\-_]+', html)
    if m:
        img_url = m.group(0)
        print("Found logo URL:", img_url)
        # download the image
        urllib.request.urlretrieve(img_url, "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/emola-logo-C2o5W9tY.png")
        print("Downloaded real E-mola logo from Play Store!")
    else:
        print("Logo URL not found.")
except Exception as e:
    print("Error:", e)
