# dictionary is a collection of key value pair separated by comma's in a curly bracket
'''syntax:
dict={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3
     }                   "'''

'''properties:-
    1. it is unordered
    2.it is mutable , it means it can be updated
    3.it is indexed
    4.it cannot have a duplicate key  '''


dict={
    "name":"sagar",
    "class":"10th",
    "marks":[20,20,50],
    "avg":30,
    "another_dict":{'name':'rahul','class':'11th'} # another dict in the main dict
}
print(dict["name"])
print(dict["class"])
print(dict["marks"])
print(dict["avg"])
print(dict)
print(dict["another_dict"]['name'])
print(dict["another_dict"])
dict["marks"]=[60,70,80] # here we can updated marks value
print(dict["marks"])
