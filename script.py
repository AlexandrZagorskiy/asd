#!/usr/bin/python3
import firstsite
import secondsite
import json

result = firstsite.first_site_json() + secondsite.second_site_json()

with open('parsed_data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4, sort_keys=True)

print("Work complete!")
