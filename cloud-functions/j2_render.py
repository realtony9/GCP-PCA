#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader

#imports from yaml
import yaml

# Load data from YAML file
config = yaml.full_load(open('./cloud-functions/0_cf-storage.yaml'))

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('./cloud-functions/1_create-cloudFunction-1.j2')

#Render the template with data and print the output
sourceFile = open('./cloud-functions/output_create-1.txt', 'w')
print(template.render(config), file = sourceFile)
sourceFile.close()