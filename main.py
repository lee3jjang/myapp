import yaml

with open('.github/workflows/python-package.yml') as f:
    members = yaml.load(f, Loader=yaml.FullLoader)

print(members)