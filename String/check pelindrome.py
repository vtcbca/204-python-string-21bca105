Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("Enter Strings. - Use Space To Seperate Words - : ")
b=[]
for i in a.split():
    if i==i[::-1]: 
        b.append(i)
print()
for i in range(len(b)):
    print(b[i])
print()
print("Total {} Pelindrome Words in String: {}".format(len(b),b)) 