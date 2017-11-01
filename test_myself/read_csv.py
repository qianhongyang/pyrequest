
import configparser

# filename = 'D:\pyrequest-master\config\\base_url.csv'
# with open(filename,'r') as f:
#     for i in f.readlines():
#         print (i.split()[0:2])

# /usr/bin/python

import string, os, sys



from function.read_MailConfig import Read_MailConfig
#
# # a = Read_MailConfig()
# # b = a.getOption()
# # print(b)
#
mail = Read_MailConfig()
a =  mail.get_email(name="a")
print(type(a))
ai = int(a)
# print(from_)
b=2
c = ai - b
print(c)

x = 1
y = 3
print(x+y)

