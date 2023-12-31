#Declare an empty list
a = [] ;      
print(a);

#Declare a list with more than 5 items
a=[1,2,3,'liza','t','a'];
print(a);

#Find the length of your list
print(len(a));
#Get the first item, the middle item and the last item of the list
print(a[0]);
last =a[len(a)-1];
print(last);
middle = int((len(a)/2)) 
print(a[middle])
 
 #Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
detail=['liza',20,155,'unmarried','jetpur'];
print(detail)
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google',' Microsoft', 'Apple', 'IBM', 'Oracle' ,' Amazon'];
#Print the list using _print()_
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print(it_companies[0]);
last =it_companies[len(it_companies)-1];
print(last);
middle = int((len(it_companies)/2)) 
print(it_companies[middle])
 #Print the list after modifying one of the companies
modify=it_companies[0]='TCS';
print(modify)
#Add an IT company to it_companies
#Insert an IT company in the middle of the companies list
it_companies.insert(middle, 'IT')
print(it_companies)
#Change one of the it_companies names to uppercase (IBM excluded!)
uper=it_companies[1].upper();
print(uper)

#Join the it_companies with a string '#;&nbsp; '
join = '#;&nbsp;'.join(it_companies)
print(join)

#Check if a certain company exists in the it_companies list.
find='Apple'
if find in it_companies: 
    print("find") 
else: 
    print("not find")
   # Sort the list using sort() method

it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
    

#Slice out the first 3 companies from the list
first=it_companies[:3]
print(first)
 #Slice out the last 3 companies from the list
last=it_companies[-3:]
print(last)
#Slice out the middle IT company or companies from the list
first1 = (len(it_companies) - 3) // 2
last1 = first1 + 3
# Slice out the middle 3 companies
middlle1 = it_companies[first1:last1]
print(middlle1)

 #Remove the middle IT company or companies from the list
remove_middle = it_companies.pop(middle)
print("Removed middle element:", remove_middle)

#Remove the first IT company from the list
remove_first=it_companies.pop(0)
print(remove_first)
print(it_companies)

#Remove the last IT company from the list

remove_last=it_companies.pop(-1)
print(remove_last)
print(it_companies)

 #Remove all IT companies from the list
 #Destroy the IT companies list
it_companies.clear();
print(it_companies)


# Join the following lists:

#     ```py
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
#     ```
    
    
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
join = front_end + back_end
print(join)


full_stack=join
print(full_stack)
index = front_end.index('Redux')


front_end.insert(index + 1, 'Python')
front_end.insert(index + 2, 'SQL')

print(front_end)
#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min1=min(ages)
print("min",min1)
max=max(ages)
print("max",max)
 #Add the min age and the max age again to the list
ages.append(min1)
ages.append(max)
print(ages)
#Find the median age (one middle item or two middle items divided by two)
middle_age = int((len(ages)/2)) 
print(int(ages[middle_age])/2)
 #Find the average age (sum of all items divided by their number )
avg=sum(ages)/len(ages)
print("avg",avg)
#Find the range of the ages (max minus min)
range=max-min1
print(range)
#Compare the value of (min - average) and (max - average), use _abs()_ method
min_avg=min1-avg
max_avg=max-avg
print(abs(max_avg))
print(abs(min_avg))

country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
c_middle=int((len(country)/2))
print(country[c_middle])
#Divide the countries list into two equal lists if it is even if not one more country for the first half.

first_half = country[:c_middle]
second_half = country[c_middle:]

print("First Half:", first_half)
print("Second Half:", second_half)
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
print(scandic_countries=second_half)