from jinja2 import Template
import json

with open('template.html') as f:
  content = "".join(f.readlines())

with open('data.json') as f:
  data = json.load(f)

t = Template(content)

with open('index.html', 'w+') as f:
  f.write(t.render(data))

print("Done")
