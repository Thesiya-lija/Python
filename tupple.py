#Create an empty tuple
tuple=()
print(tuple)
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=('monika','amisha','pinal')
brothers=('ravi','naimish','raj')
print(sisters)
print(brothers)
#Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers
print(siblings)
#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father=("DhanjiBhai")
mother=('SangitaBen')
family_members=(father,mother,*siblings)
print(family_members)
#Unpack siblings and parents from family_members
(father,mother,*siblings)=family_members
print(father)
print(mother)
print(siblings)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Apple','Banana','WaterMelon')
vegetables=('Cucumber','Pumpkin','Tomato')
animal=('Lion','Tiger','Bear')
#Change the about food_stuff_tp  tuple to a food_stuff
food_stuff_tp=fruits+vegetables+animal
print(food_stuff_tp)


#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
middle=int(len(food_stuff_lt)/2)
print(food_stuff_lt[middle])
#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

#Delete the food_staff_tp tuple completely
print(food_stuff_lt.clear())
#Check if an item exists in  tuple:
#- Check if 'Estonia' is a nordic country
#- Check if 'Iceland' is a nordic country
 # nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


nordic_countries=('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print('Estonia is a nordic country.')
else:
    print('Estonia is not a nordic country.')
if 'Iceland' in nordic_countries:
 print('Iceland is a nordic country.')
else:
 print('Iceland is not a nordic country.')



