#A).Create a list and apply methods (append, extend, remove, reverse), arrange 
#created list in ascending and descending order


List=[10,20,4,51,3]
List.append(7)
print(list)
extend=['liza']
List.extend(extend)
print(List)
List.remove("liza")
print(List)
reversed = list(reversed(List))
print(reversed)
print(sorted(List))
List.sort(reverse=True)
print(List)


#B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", 
#"orange"]]
#From above list get word “orange” and “Python” & repeat this list five times without 
#using loops.
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", 
"orange"]]
orange = List1[-1][-1]
python = List1[4][0]
result = [List1] * 5
print("orange:", orange)
print("Python:", python)
print("Repeated list five times:",result)

# C) Create a list and copy it using slice function
copy = [1, 2, 3, 4, 5]
copy1 = copy[:]
copy[0] = 1
print("Original list:", copy)
print("Copied list:", copy1)
# D) Create a tuple and apply different type of mathematical operation on it (Sum, 
# Maximum, minimum etc.).
tuple=(2,5,7,8)
sum=sum(tuple)
print(sum)
max=max(tuple)
print(max)
min=min(tuple)
print(min)

    