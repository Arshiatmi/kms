import os
import builtwith
import requests
import urllib.parse
from .ig import *
from .hash import *
from .list import *
from colorama import Fore
from .page_inspect import *
from .bypass import *
from .classes import *

def find_admin_php(address):
    ok_addresses = []
    for i in list_admin_finder_php:
        #Send A Request To Target
        request = requests.get(address + "/" + i)
        #check If Target Valid Or Not
        if request.status_code == 200:
            ok_addresses.append(address + "/" + i)
    return ok_addresses

def find_admin_asp(address):
    ok_addresses = []
    for i in list_admin_finder_asp:
        #Send A Request To Target
        request = requests.get(address + "/" + i)
        #check If Target Valid Or Not
        if request.status_code == 200:
            ok_addresses.append(address + "/" + i)
    return ok_addresses

def find_cms(address):
    #check That Address builtwith What?
    #Maybe Joomla Maybe ...
    return builtwith.builtwith(address)


def url_encode(string):
    #Encode Url
    return urllib.parse.quote(string)
