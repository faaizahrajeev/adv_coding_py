# sorted(listName) doesn't change in place but listName.sort changed the list 

# if you do list1 = list2 and change list2, list1 changes too
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1) # [1, 2, 3, 4]
print(list2) # [1, 2, 3, 4]

# if you do list1 = list2.copy() and change list2, list1 doesn't change
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1) # [1, 2, 3]
print(list2) # [1, 2, 3, 4]

# also, if you do list1 = list2[:] or list1 = list(list2) and change list2, list1 doesn't change

# list comprehension
a = [1,2,3,4,5]
b = [x*x for x in a]
print(b)
# [::-1] to reverse



# packing, unpacking tuples
myTuple = "faai", 20, "dubai"
name, age, city = myTuple
print(name) # faai
print(age) # 20
# if you had name, age = myTuple, you'd get ValueError: too many values to unpack (expected 2)

myTuple = (1,2,3,4,5)
a, *b, c = myTuple
print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5

# it takes much longer to unpack a list than a tuple




# mydict[key_name]
# mydict.values() 
# mydict.keys() 
# key, value in mydict.items() 
# mydict.pop(key_name) and mydict.popitem() removes the last item
# del mydict[key_name] and del mydict to delete the whole dictionary

mydict = {"name": "faai", "age": 20, "city": "dubai"}
mydict1 = {"name": "faai", "age": 20, "email": "faai@gmail.com"}
mydict.update(mydict1)
print(mydict) # {'name': 'faai', 'age': 20, 'city': 'dubai', 'email': 'faai@gmail.com'}