# li=[1,2,"f",'g','ef',4,]
# # print(li)
# for items in li:
#     print(items)

# ele= input("enter list elements")
# li=ele.split()
# print(li)

# li=list(input("enter list elements").split())
# print(li)

# tup=tuple(input("enter elements of tuple").split())
# print(tup)

# se=set(input("enter elements of set").split())
# print(se)

my_dict = {}

print("Enter key-value pairs (leave key blank to stop):")

while True:
    key = input("Enter key: ")
    if key == "":
        break
    value = input("Enter value: ")
    my_dict[key] = value

print("Dictionary created:", my_dict)