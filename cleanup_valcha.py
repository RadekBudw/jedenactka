with open('build_verze_a.py', 'r', encoding='utf-8') as f:
    va = f.read()

va = va.replace('uppercase tracking-wider">Loděnice Valcha</span>', 'uppercase tracking-wider">Základna Valcha</span>')
va = va.replace('// Loděnice Valcha', '// Základna Valcha')
va = va.replace('alt="Skauti v loděnici na řece"', 'alt="Skauti na základně Valcha"')
va = va.replace('src="foto_3.jpg" alt="Skauti na základně Valcha"', 'src="zonerama_valcha.jpg" alt="Skauti na základně Valcha"')

with open('build_verze_a.py', 'w', encoding='utf-8') as f:
    f.write(va)

with open('build_verze_b.py', 'r', encoding='utf-8') as f:
    vb = f.read()

vb = vb.replace('alt="Loděnice Valcha"', 'alt="Základna Valcha"')
vb = vb.replace('src="foto_3.jpg" alt="Základna Valcha"', 'src="zonerama_valcha.jpg" alt="Základna Valcha"')
vb = vb.replace('// Loděnice Valcha', '// Základna Valcha')

with open('build_verze_b.py', 'w', encoding='utf-8') as f:
    f.write(vb)

print("Applied clean-ups to build_verze_a.py and build_verze_b.py")
