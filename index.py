import os

files = sorted(f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html')
with open('index.html', 'w', encoding='utf-8') as idx:
    idx.write("""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Site Index</title>
  <style>
    body { font-family: sans-serif; padding: 2rem; }
    ul { list-style: none; }
    li + li { margin-top: .5rem; }
  </style>
</head>
<body>
  <h1>Pages</h1>
  <ul>
""")
    for fn in files:
        idx.write(f'    <li><a href="{fn}">{fn.replace(".html","").title()}</a></li>\n')
    idx.write("""  </ul>
</body>
</html>
""")

