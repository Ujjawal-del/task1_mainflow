# LIST, DICTIONARY AND TUPPLE

fruits = ["apple","orange",2,3,True]
print(fruits)

fruits.append(8)
print(fruits)

fruits.pop(2)
print(fruits)

fruits.insert(2,"grapes")
print(fruits)  
#Hence list are muttable and store a set of value of any data type

#DICTIONARY -> MUTTABLE
a = {
"key": "value",
"har": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]

#dictionary methods
new_dictionary = a.copy()
print(new_dictionary)

print(a.get("list"))

print(a.keys())

value1 = a.pop("har")
print(a)
print(new_dictionary)

#TUPPLE-> immutable
tup = (1,3,5,True,"man")
print(tup)
tup1 = (2,False,"enjoy")

#tupple methods
print(tup[3])
print(tup[-1])
print(tup.index("man"))
print(tup[1:4])
print(tup + tup1)
