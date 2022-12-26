from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://mbasic.facebook.com'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣Enter 2 step google code : "))

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()

    

    

def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()
    print("\033[1;32;40m", end = "")
    print ("\n[[ The Bunny Mer'Chant Creation  ]]\n")
    e = datetime.datetime.now()
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))

print("\033[1;33;40m", end = "")
print('===========================================================')
print("-[ ✪✿✪✿✪ The Bunny Mer'Chant Creation =V ✪✿✪✿✪ ]-]")
print('===========================================================')

emailx=str(input("➥✪➣Enter Username or Email : "))

pwx =str(input("➥✪➣Ente your password : "))

aclass()

msg4=str(input("➣The post link : "))

msg5=str(input("➣Noepad link : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Delay time (in seconds) : "))

os.system('clear')

sys.stdout.flush()

print("\033[1;33;40m", end = "")
print('===========================================================')
print("-[ ✪✿✪✿✪ The Bunny Mer'Chant Creation =V ✪✿✪✿✪ ]-]")
print('===========================================================')

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(line)

            print('Comment Sent Successfully - ', line)

            count += 1

            if count % 10 == 0:

                sleep(1)                                         
