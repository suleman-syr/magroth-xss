#!/usr/bin/env python3
import requests
import getopt
import sys
from bs4 import BeautifulSoup
import os
import threading
import time

target = ''
params = []
path = []
XssPayloads = ''
listPayload = []

def usge():
    print('[*] morgothXss is a tool for scaning web application if any Xss ....')
    print('[*] you can using your wordlist or use our wordlist ..')
    print('[*] used : morgxss -u https://example.com -p payloadXss.txt')
    print('     -u or --url : domain website')
    print('     -p or --payload : list of your payload')
    print()
    print('created by Dr-shell morgoth *_*')


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def start():
    # A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)



os.system('clear')
start()


def main():
    global target
    global path
    global params
    global XssPayloads
    global listPayload

    try:
        opt, arg = getopt.getopt(sys.argv[1:], 'hu:p:', ['help', 'url', 'payload'])
    except getopt.GetoptError as error:
        usge()

    for o, a in opt:
        if o in ('-h', '--help'):
            usge()
        if o in ('-u', '--url'):
            target = a
        if o in ('-p', '--payload'):
            XssPayloads = a

    params = getparam(target)
    path = getpath(target)
    fullpath = GetFinalePath(path, params)
    checkPayload(XssPayloads)
    thred_req = threading.Thread(target=requester, args=(fullpath,listPayload))
    thred_req.start()

    # requester(fullpath, listPayload)


def getparam(t):
    try:
        res = requests.get(t)
        soup = BeautifulSoup(res.content, 'html.parser')
        for inputs in soup.findAll('input'):
            return inputs.get('name')
    except:
        print('Error in connection or URL Not valid in website ...')


def getpath(t2):
    try:
        res = requests.get(t2)
        soup = BeautifulSoup(res.content, 'html.parser')
        for forms in soup.findAll('form'):
            return forms.get('action')
    except:
        print('Error in connection or URL Not valid in website ...')


def GetFinalePath(pt, par):
    global target

    FinaleTarget = f'{target}' + f'{pt}' + '?' + f'{par}='
    return FinaleTarget


def checkPayload(Pa):
    global listPayload
    if Pa.endswith('.txt'):
        with open(Pa, 'r') as f:
            for i in f:
                listPayload.append(i)
    else:
        if Pa.startswith('\'') and Pa.endswith('\''):
            listPayload.append(Pa)
            print(listPayload)
        elif Pa.startswith('<') and Pa.endswith('>'):
            print('error you need to put your payload in \' \' ')


def requester(url, wordlist):
    valid_payload = []
    for i in range(len(wordlist)):
        try:
            attackerPath = f'{url}{wordlist[i]}'
            res = requests.get(attackerPath)
        except:
            print('Error in connection ...')

        print(f'[*] testing : {attackerPath}', '')
        if wordlist[i] in res.text:
            CRED = '\033[32m'
            CEND = '\033[0m'
            print(CRED + f'valid => {attackerPath}' + CEND)
            valid_payload.append(attackerPath)
        else:
            CRED = '\033[91m'
            CEND = '\033[0m'
            print(CRED + "Error, Payload is not valid!" + CEND)


if __name__ == '__main__':
    main()
