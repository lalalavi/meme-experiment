import os
import re 

print(os.getcwd())
os.listdir('otreememes/_static/LR')
memelist = os.listdir()
pattern = r"meme(?P<number>\d{3})\.jpg"
m = re.match(pattern, "meme200.jpg")
print(m)
# you are telling the pattern of the files inside of the folder, in my case a string...
# ...that says meme, then a THREE DIGIT number + .jpg, and then you group it by the number
numberito = int(m.group("number"))
print(numberito)