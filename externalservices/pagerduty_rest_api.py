#!/usr/bin/env python
#
#### External Services Monitoring Scripts
#
#
# Author: Matthew Macdonald-Wallace
# (c) DevOpsGuys Ltd 2016
# Licensed under the MIT Software License
import sys
import json
import requests

status_url = "https://33yy6hwxnwr3.statuspage.io/api/v2/summary.json"
status_data = requests.get(status_url)
status_json = json.loads(status_data.text)

exit_code = 3
message = "UNKNOWN"

for component in status_json['components']:
    if component['name'] == 'REST API & Web Application':
        if component['status'] == 'operational':
           exit_code = 0
           message = "Pager Duty REST API & Web Application is online"
        else:
           exit_code = 2
           message = "Pager Duty REST API & Web Application is experiencing issues"

print message
sys.exit(exit_code)
