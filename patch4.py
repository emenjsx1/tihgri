import re

js_file = "c:/Users/PRECISION/Downloads/skills_todas_2/tigrinho_moz/assets/index-BFKrrs40-v2.js"
with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

new_hs = """HS=({onCheckout:e})=>{b.useEffect(()=>{var s=document.createElement("script");s.src="https://scripts.converteai.net/e7a84390-3678-4782-a86c-6a648195ed28/players/6a271f7604ab345fc2dccc0e/v4/player.js";s.async=!0;document.head.appendChild(s);},[]);return p.jsxs(de.div,{initial:{opacity:0,y:20},animate:{opacity:1,y:0},exit:{opacity:0,y:-20},className:"relative flex flex-col items-center justify-start min-h-svh p-4 space-y-4",children:[p.jsx("h2",{className:"text-xl font-black font-display text-primary text-center uppercase leading-tight px-2",children:"Assista este vídeo pra saber como receber o seu pagamento"}),p.jsx("div",{className:"w-full bg-card/90 backdrop-blur-xl rounded-2xl overflow-hidden gold-border",children:p.jsx("vturb-smartplayer",{id:"vid-6a271f7604ab345fc2dccc0e",style:{display:"block",margin:"0 auto",width:"100%"}})})]})},CM="""

content = re.sub(r'HS=\(\{onCheckout:e\}\)=>\{.*?\},CM=', new_hs, content, flags=re.DOTALL)

# Add another cache buster to CSS/JS again just to be 100% sure the user sees it without struggling
with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced HS component successfully")
