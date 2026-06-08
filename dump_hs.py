js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40-v2.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("HS=({onCheckout:")
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("Not found")
