import json, re, os

with open('leaders.json', 'r', encoding='utf-8') as f:
    raw_leaders = json.load(f)

clean_list = []

for idx, item in enumerate(raw_leaders):
    raw = [l.strip() for l in item['raw'] if l.strip()]
    name = raw[0]
    if name.startswith('Mag. iur.'):
        name = 'Mag. iur. Christopher Alexander De La Cruz'
    
    nickname = ''
    role_lines = []
    i = 1
    if i < len(raw) and raw[i] in ['–', '-']:
        i += 1
    
    if i < len(raw) and not raw[i].startswith('tel') and '@' not in raw[i] and 'Má na' not in raw[i]:
        nickname = raw[i].replace('–', '').replace('-', '').strip()
        i += 1
    
    while i < len(raw) and '@' not in raw[i] and not raw[i].startswith('tel') and 'Má na' not in raw[i]:
        if raw[i] not in ['–', '-']:
            role_lines.append(raw[i])
        i += 1
    
    role = ' '.join(role_lines) if role_lines else 'Lodivod'
    
    email = ''
    phone = ''
    starosti = ''
    kvalifikace = ''
    
    for line_idx, line in enumerate(raw):
        if '@' in line:
            email = line
        elif 'tel.' in line or re.search(r'\d{3}\s*\d{3}\s*\d{3}', line):
            phone = line.replace('tel.:', '').replace('tel.', '').strip()
        elif 'starosti:' in line.lower() and line_idx + 1 < len(raw):
            starosti = raw[line_idx + 1]
        elif 'kvalifikace:' in line.lower() and line_idx + 1 < len(raw):
            kvalifikace = raw[line_idx + 1]
            
    if idx == 0:
        paluba = 'Vedení oddílu'
    elif idx <= 15:
        paluba = 'Toulavá smečka'
    else:
        paluba = 'Bárka'
        
    avatar_file = f'avatar_{idx+1}.jpg'
    # Check if avatar file exists
    has_avatar = os.path.exists(os.path.join('verzeA', 'avatars', avatar_file))
    
    clean_list.append({
        'id': idx + 1,
        'name': name,
        'nickname': nickname,
        'role': role,
        'paluba': paluba,
        'email': email,
        'phone': phone,
        'starosti': starosti,
        'kvalifikace': kvalifikace,
        'avatar': f'avatars/{avatar_file}' if has_avatar else ''
    })

with open('vedeni_clean.json', 'w', encoding='utf-8') as f:
    json.dump(clean_list, f, ensure_ascii=False, indent=2)

print('Successfully cleaned and saved', len(clean_list), 'leaders.')
