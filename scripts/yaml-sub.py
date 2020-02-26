_author__ = 'tkraus-m'

import yaml, os
import sys, getopt
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()
# add long and short argument
parser.add_argument('--server', '-s')
parser.add_argument('--repo', '-r')
parser.add_argument('--tag', '-t')
# read arguments from the command line
args = parser.parse_args()

print("Supplied Server Argument is = ", args.server)
print("Supplied Repo Argument is = ", args.repo)
print("Supplied Tag Argument is = ", args.tag)

with open('/Users/kraust/sandbox/yaml-work/kustomization.yaml') as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)
    print("The Existing kustomization.yaml newTag Value is . . ." + doc['images'][0]["newTag"])
    # for key, value in doc.items():
        #print(key + " : " + str(type(value)) + " = " + str(value))
        #if type(value) is list:
            #print(str(len(value)))
    
doc['images'][0]["newTag"] = args.tag

print("The New kustomization newTag Value is . . ." + doc['images'][0]["newTag"])
with open('/Users/kraust/sandbox/yaml-work/kustomization.yaml', 'w') as n:
    yaml.dump(doc, n)
