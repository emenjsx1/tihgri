import re

js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40-v2.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# find iframe or video elements
matches = re.findall(r'.{0,50}(?:iframe|vturb|video|vsl|player).{0,50}', content, flags=re.IGNORECASE)
for i, m in enumerate(set(matches[:20])):
    print(f"[{i}] {m}")
