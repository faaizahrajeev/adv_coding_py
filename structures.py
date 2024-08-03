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



set1 = {1, 2, 3, 4, 5}
# sets are unordered and unindexed
myset = set("hello Faai")
print(myset) # {'F', 'a', 'i', 'e', 'l', 'o', 'h', ' '} order changes every time




# string slices string1[2:5]
# mystring.strip() removes whitespaces from the beginning and end
# .upper() .lower() .replace("old", "new") 
# .split(" ") -- into a list 
# .join(mylist) -- combines a list into a string
# .find("substring")-- first index where it's found 
# .count("substring") .startswith("substring") 
# .endswith("substring") .isalnum() .isalpha() .isdigit() .islower() 
# .isupper() .istitle() .isspace() .capitalize() .lstrip() .rstrip() 

var = "hello"
myString = "%s im faaizah" % var # placeholder
print(myString) # hello im faaizah

# %d for integers, %f for floats, %s for strings

# .format() method
myString = "hello {} im faaizah".format(var)
print(myString) # hello hello im faaizah

myString1 = "hello {0} im {1}".format(var, "faaizah")
print(myString1) # hello hello im faaizah

var1 = 3.14159
myString2 = "the value of pi is {:.2f}".format(var1)
print(myString2) # the value of pi is 3.14

# f-strings
myString3 = f"hello {var} im faaizah"
print(myString3) # hello hello im faaizah




# collections : Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaabbbbbcccc"
myCounter = Counter(a)
print(myCounter) # Counter({'a': 5, 'b': 5, 'c': 4})
print(myCounter.most_common(1)[0][0]) # [('a', 5)]
# 1 is the number of most common items u wanna see
print(myCounter.items()) # dict_items([('a', 5), ('b', 5), ('c', 4)])

from collections import namedtuple
Point = namedtuple("Point", "x, y") # class name, attributes
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)
print(pt.x) # 1
print(pt.y) # -4


from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["z"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
print(ordered_dict) # OrderedDict([('z', 1), ('b', 2), ('c', 3)])