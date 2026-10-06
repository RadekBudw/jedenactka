for fname in ['build_verze_a.py', 'build_verze_b.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('src="{prefix}logo_emblem.png"', 'src="logo_emblem.png"')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f'Fixed {fname}')
