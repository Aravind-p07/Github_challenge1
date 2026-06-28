#homework 
#find aLARGEST & SMALLEST from list without any min, max functions
a=[100,-6,589,10,2,3,-999,18,23,9]


#find aLARGEST & SMALLEST from list without any min, max functions
larger_num=a[0] #assign first value as a benchmark
smaller_num=a[0]

for i in a[1:] :
    if i> larger_num: # if element of the list is larger than benchmark set the elemnt as new benchmark
        larger_num=i
        
    if i<smaller_num: # if element of the list is smaller than benchmark set the element as new benchmark
        smaller_num=i

print("The largest number of the given list is :-", larger_num) 
print("The smallest number of the given list is :-",smaller_num)

   
    
