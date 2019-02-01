#!/usr/local/bin/python3

import random
import requests
import argparse
import json

query = "https://developers.zomato.com/api/v2.1/search?entity_id=163279&entity_type=subzone&lat=42.4823708&lon=-71.2068706&radius=3000&establishment_type=281"
headers={'user-key': '<api-key>'}

parser = argparse.ArgumentParser(description='Pick out a place to eat.')
parser.add_argument("--type", required=False)

args, etc = parser.parse_known_args()

if args.type is not None:
    query += "&q={0}".format(args.type)

response = requests.get(query, headers=headers)

json = response.json()
restaurants = json['restaurants']

pick = random.randint(0,len(restaurants)-1)
print (restaurants[pick]['restaurant']['name'] + "\t(Picked from {0} restaurants)".format(len(restaurants)))
