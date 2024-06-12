#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader

#imports from yaml
import yaml

# Load data from YAML file
config = yaml.full_load(open('./lb-http-config/0_lb-http.yaml'))

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('./lb-http-config/6_lb-forwarding-1.j2')

#Render the template with data and print the output
sourceFile = open('./lb-http-config/output_forwarding-1.txt', 'w')
print(template.render(config), file = sourceFile)
sourceFile.close()