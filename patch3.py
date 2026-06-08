js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40-v2.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('tiger-mascot-BjAPybxp.jpeg', 'tiger-mascot-v2.jpeg')

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated image path in JS")
