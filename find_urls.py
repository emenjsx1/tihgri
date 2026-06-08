import re

js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

urls = re.findall(r'https?://[^\s\"\']+', content)
for u in set(urls):
    if any(ext in u.lower() for ext in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp']):
        print(u)
