import re 

lines = int(input())
inp = ""
for line in range(lines):
    inp += input().strip() + " "

# str_ = "assd@gmail.com and isdj sdg sdf@dfsgg.ocm asdsdfs s dfj"
# print(';'.join(sorted(set(re.findall('\w+@\w+.\w+', inp)))))
# print(';'.join(sorted(set(re.findall('^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.\w{2,4}$', inp)))))
print(';'.join(sorted(set(re.findall('(\w*\.?\w+@(?:[a-z]+\.)+\w+)', inp)))))
