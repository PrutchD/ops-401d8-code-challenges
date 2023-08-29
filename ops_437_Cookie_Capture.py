#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 37
# Author:                       David Prutch
# Date of latest revision:      08/29/2023
# Purpose:                      This script is taken from a starter template.
#                               Modifications I have made begin on line # 39 and include the folowing additions
                                # - Send the cookie back to the site and receive a HTTP response
                                # - Generate a .html file to capture the contents of the HTTP response
                                # - Open it with Firefox

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')



# Additions begin below

# Function to send the cookie and capture the HTTP response
def send_cookie_and_capture_response():
    targetsite = "http://www.whatarecookies.com/cookietest.asp"
    headers = cookie 

    response = requests.get(targetsite, headers=headers)
    return response.text

# Function to generate an HTML file and write the HTTP response contents to it
def generate_html_file(content):
    with open('response.html', 'w') as f:
        f.write(content)
        f.close()

# Function to open the generated HTML file with Firefox
# Make sure Firefox is the default browser
def open_html_with_firefox():
    import webbrowser
    webbrowser.get("firefox").open("response.html")

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)
response_content = send_cookie_and_capture_response()
generate_html_file(response_content)
open_html_with_firefox()
# Stretch Goal
# - Give Cookie Monster hands