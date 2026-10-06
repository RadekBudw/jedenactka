import re

def analyze_file(filename):
    print("=== File:", filename)
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        m = re.findall(r'id=["\']([^"\']+)["\']', line)
        if m:
            print(f"Line {i+1}: id={m}")

analyze_file('verzeA/index.html')
analyze_file('verzeB/index.html')
