import re

js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# The JS uses:
# const n=e==="mz"?dM:FS;
# We want to flip this so it defaults to MZ if not specified, or just always use dM.
# Actually, the easiest is to just change e==="mz"?dM:FS to e!=="ao"?dM:FS or simply always use dM.
content = content.replace('const n=e==="mz"?dM:FS;', 'const n=dM;')
content = content.replace('US=b.createContext(FS)', 'US=b.createContext(dM)')

# Let's also check for any explicit "Kz" or "Kwanza"
# the code has xt(1e3,t) which formats using currency from context.
# So changing the context to dM (Mozambique config) will automatically use MT, E-Mola, M-Pesa.

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Patched JS file to use Mozambique config by default.")
