import os
d=r'c:\Users\Admin\Desktop\college-website - Copy\college_backend\templates\core'
for f in os.listdir(d):
    if f.endswith('.html'):
        p = os.path.join(d, f)
        with open(p, 'r', encoding='utf-8') as file:
            c = file.read()
        c = c.replace("\\'", "'")
        with open(p, 'w', encoding='utf-8') as file:
            file.write(c)
