import re
a="the rain in spain mainly in the plains"
x=re.findall(r"rain|stays",a)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
