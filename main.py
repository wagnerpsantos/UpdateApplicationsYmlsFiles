## Import the modules to handle JSON & YAML
import yaml
import json

## Create a variable to hold the data to import
os_list = {}

## Read the YAML file
with open("application.yml") as infile:
  # Marshall the YAML into the variable defined above 
  os_list = yaml.load(infile, Loader=yaml.FullLoader)     
  # Print the List to the console. 
  print(os_list)
  
with open("application.json", 'w') as outfile:
  # Marshall the JSON, setting "indent" makes the file more readable 
  json.dump(os_list, outfile, indent=4) 
  print("JSON file written.")