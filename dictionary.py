#Create  an empty dictionary called dog
dog={}
print(dog)
#Add name, color, breed, legs, age to the dog dictionary
dog={
'name':'Buddy',
    'color': 'Brown',
    'breed': 'Labrador Retriever',
'legs':4, 
'age':2}
print(dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name':'liza',
    'last_name':'Thesiya',
    'gender':'Female',
    'age':20,
    'marital status':'unmarried',
    'skills':['Programming','Communication'],
    'country':'india',
    'city':'piplava',
        'address':'piplva,jetpur'
    }
print(student)
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
print(student['skills'])
if  type(student['skills']) ==list:
    print("list")
else:
    print('not list')
    #Modify the skills values by adding one or two skills
student['skills'][0]='Designing'
print(student['skills'])
    #Get the dictionary keys as a list
print(student.keys())
    #Get the dictionary values as a list
print(student.values())
#Change the dictionary to a list of tuples using _items()_ method
list=list(student.items())
print(list)
#Delete one of the items in the dictionary
delete=(student.pop('city'))
print(delete)
print(student)
#Delete one of the dictionaries
student.clear()
print(student)

    