from .get_char_code import *

def part(your_string,splitter):
    answers = []
    #I Named in_splitter_string To "String Store Variable"
    in_splitter_string = ""
    #I Named in_splitter Variable To "Check Variable"
    in_splitter = False
    #Do Something With All Characters
    for char in your_string:
        #Check If Character Is splitter Or Not
        #if It Was:
        if char == splitter:
            #Check If Current Character Is Between 2 splitter Or Not
            if not in_splitter:
                #If It Wasnt Change The "Check Variable" Value
                in_splitter = True
            else:
                # If It Was, Change The "Check Variable" Value
                in_splitter = False
                #Add String To answers Array
                answers.append(in_splitter_string)
                #Again Clear The "String Store Variable"
                in_splitter_string = ""
        else:
            #If Character Wasnt splitter
            if in_splitter:
                #Check If Between To splitter That If It Was True
                #This Will Be Runned:
                in_splitter_string += char
                #In Fact If Now We Are Between Two splitter,
                #We Will Add Current Character To "String Store Variable"
    return answers

def from_char_code(string):
    #Get Part Of String That Exists Between Two (")
    parts = part(string,"\"")
    answer = ""
    allofanswers = []
    #Do Something With All Parts That Exists Between Two (")
    for part in parts:
        #Replaces The Characters With Ascii Codes
        for x,y in char_codes.items():
            part = part.replace(y," " + x + " ,")
            answer = part
        #Give A Clear Value!
        #If You Check The Loop You Can Underestand That Program
        # Give A Resault Like That:
        # "110 , 120 , 140 ,"
        # As You See Contains Two Addtion Character!
        # We Are Removing Them Here:
        answer = answer[:-2]
        #Bring answer Between '(' And ')'
        answer = "(" + answer + ")"
        allofanswers.append(answer)
    #Add String.fromCharCode To The answer
    fin = ["String.fromCharCode" + i for i in allofanswers]
    #Do Something With All Parts That Exists In Two (")
    for i in parts:
        for j in fin:
            #We Create New String That Replace
            #The Last String With New Encoded String.
            string = string.replace(i,j).replace("\"","")
    #Now, We Will Do Every Thing For (') That We Did For (") Too!
    parts = part(string,"\'")
    answer = ""
    allofanswers = []
    for part in parts:
        for x,y in char_codes.items():
            part = part.replace(y," " + x + " ,")
            answer = part
        answer = answer[:-2]
        answer = "(" + answer + ")"
        allofanswers.append(answer)
    fin = ["String.fromCharCode" + i for i in allofanswers]
    for i in parts:
        for j in fin:
            string = string.replace(i,j).replace("\'","")
    return string
