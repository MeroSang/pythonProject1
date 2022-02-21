v1="123"
print(v1.isdecimal())

v2="①"
print(v2.isdecimal())   #False

v3="123"
print(v3.isdigit())

v4="①"
print(v4.isdigit())  #True