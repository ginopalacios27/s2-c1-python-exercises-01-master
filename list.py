numberList = [1, 2, 3]
print(numberList)

numberList = [1, "pepito", False]
""" print(numberList)
print(len(numberList))
print(dir(numberList))
print(numberList.pop())
print(numberList) """

""" tupleData = (1, 2, False)
print(dir(tupleData)) """
""" https://www.w3schools.com/python/python_lists.asp """

for item in numberList:
    print(type(item))
    if isinstance(item, int):
        print("is a number")
    elif isinstance(item, str):
        print("is a string")
    elif isinstance(item, bool):
        print("is a bool")
