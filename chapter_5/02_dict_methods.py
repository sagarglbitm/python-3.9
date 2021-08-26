dict={
    "name":"sagar",
    "class":"10th",
    "marks":[20,20,50],
    "avg":30,
    "another_dict":{'name':'rahul','class':'11th'}, # another dict in the main dict
    1: 2 # it is also a key:value pair
}
print(dict.keys()) # it print keys of a dictionary
print(type(dict.keys())) # it print type which is a dictionary type
print(list(dict.keys())) # it print keys value as alist ,it is also called type_conversion
print(dict.values()) # it print value of a dictionary
print(dict.items()) # it print the dictionary in form tupples
update_dict={"score":"100","century":"02"
}
dict.update(update_dict)# here we first create a dict and then,we update it
print(dict)
print(dict.get("avg")) # it also gives value but if that key is not present,it retrn none
# whereas print(dict["avg"]) throws an error  if key not present