def reverseString(string):
    if string == "":
        return string
    else:
        # print("{:3} | {:3} | {:3} |".format(string, string[1:], string[0]))
        return reverseString(string[1:]) + string[0]


print(reverseString("python"))


# reverseString('abc')                       #string = abc
# =reverseString('bc') + 'a'                 #string[1:] = bc    string[0] = a
# =reverseString('c') + 'b' + 'a'            #string[1:] = c     string[0] = a
# =reverseString('') + 'c' + 'b' + 'a'
# ='cba'

# print("{:3} | {:3} | {:3} |".format(string, string[1:], string[0]))
