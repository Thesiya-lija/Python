
# A) String Operations:
#  Reverse a string, replace string with other string, merge two strings
#  Find character is in string or not without using loops
#  Split string into multiple words &characters
string = "liza"
reverse = string[::-1]
print("Reversed string:", reverse)
new_string = string.replace("liza", "Liza")
print("New string:", new_string)
string1="Thesiya"
merge=string+string1
print(merge)
Find = "Python is Programming language"
char_find= "o"
if char_find in Find:
    print(f"'{char_find}' is in the string.")
else:
    print(f"'{char_find}' is not in the string.")
split_str = "Liza,Thesiya"
words = split_str.split()
characters = [char for char in split_str]
print("Words:", words)
print("Characters:", characters)

# B) Dictionaries Operations:
#  Apply “Update, Delete, clear, popitem, pop, get, keys and values” operation in 
# dictionary.
#  Create 3 dictionaries and merge them into 1 dictionary
dict = {
    'name': 'liza',
    'age': 20,
    'city': 'Jetpur'
}
dict.update({'age': 21, 'gender': 'Male'})
print("After Update:", dict)
del dict['city']
print("After Delete:",dict)
dict.clear()
print("After Clear:", dict)
dict = {
    'name': 'liza',
    'age': 20,
    'city': 'Jetpur'
}
item = dict.popitem()
print("Popped item:", item)
print("After Popitem:", dict)
age = dict.pop('age')
print("Popped age:", age)
print("After Pop:", dict)
name = dict.get('name')
print("Name:", name)
keys = dict.keys()
print("Keys:", keys)
values = dict.values()
print("Values:", values)
dict_merge1 = {
    'name': 'Liza',
    'age': 20,
}
dict_merge2 = {
    'Gender':'Female',
    'city': 'Jetpur'
}
dict_merge3 = {
    'state':'Gujarat',
    'Country':'India'
}
merge_all={**dict_merge1,**dict_merge2,**dict_merge3}
print(merge_all)