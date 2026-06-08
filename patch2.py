import re

js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace all possible Kwanza references
content = content.replace('Kz', 'MT')
content = content.replace('KZ', 'MT')
content = content.replace('Kwanza', 'Metical')
content = content.replace('kwanza', 'metical')

# Replace IBAN and Angola references just in case
content = content.replace('IBAN', 'Número')
content = content.replace('ibanPlaceholder:"AO06 XXXX XXXX XXXX XXXX XXXX X"', 'ibanPlaceholder:"8X XXX XXXX"')
content = content.replace('ibanPrefix:"AO"', 'ibanPrefix:"MZ"')
content = content.replace('Multicaixa Express', 'M-Pesa')
content = content.replace('Pagamento por Referência', 'E-Mola')
content = content.replace('express:{label:"M-Pesa"', 'express:{label:"M-Pesa"')

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Patched all Kwanza to MT and Multicaixa to M-Pesa.")
