# match anything but a new line 

""" 
First character: 1, 2 or 3
Second character: 1, 2 or 0
Third character: x, s or 0
Fourth character: 3, 0 , A or a
Fifth character: x, s or u
Sixth character: . or ,
"""
import re 

inp = input()
print(type(inp))
Regex_Pattern = '[123][120][xs0][30Aa][xsu][\.,]'
print(str(bool(re.search(Regex_Pattern, inp))).lower())


