from .get_char_code import *

class xss:
    def __init__(self):
        self.hex_back = "%2E%2E%2f"
        self.hex_per = "%25"
        self.double_hex_back ="%252E%252E%252F"

    #Encode To Hexadecimal
    @staticmethod
    def encode_hexadecimal(string):
        ans = ""
        for char in string:
            for i,j in hexadecimal_char_codes.items():
                char2 = char.replace(j,"%" + i)
                if not char == char2:
                    ans += char2
        return ans

    #Double Encoding To Hexadecimal
    def double_encode_hexadecimal(self,string):
        one_encode = self.encode_hexadecimal(string)
        one_encode = one_encode.replace("%","%25")
        return one_encode

    #Encode Symbols To Hexadecimal
    @staticmethod
    def encode_symbol_hexadecimal(string):
        ans = ""
        for char in string:
            for i,j in hexadecimal_char_codes.items():
                if not (char.upper() in letters):
                    char2 = char.replace(j,"%" + i)
                    if not char == char2:
                        ans += char2
                else:
                    ans += char
                    break
        return ans

    #Double Encoding Symbols To Hexadecimal
    def double_encode_symbol_hexadecimal(self,string):
        one_encode = self.encode_symbol_hexadecimal(string)
        one_encode = one_encode.replace("%","%25")
        return one_encode
