'''
🚀hey @everyone  Coding Challenge: Armstrong Number Checker

Problem Statement:
Write a Python program to check whether a given number is an Armstrong number or not.

👉 A number is called an Armstrong number (also known as a narcissistic number) if the sum of its digits each raised to the power of the number of digits is equal to the number itself.

Examples:

153 → 1³ + 5³ + 3³ = 153 ✅ (Armstrong)

9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅ (Armstrong)

123 → 1³ + 2³ + 3³ = 36 ❌ (Not Armstrong)

Input:

A single integer n

Output:

Print "Armstrong Number" if it is, otherwise "Not Armstrong Number"'''

#SOLUTION

a=int(input("enter a number :- "))
a_list=list(str(a))
sum_num=0
for i in range (0,len(a_list)):
    sum_num+= int(a_list[i])**len(a_list)
if sum_num==a:
    print(f"Entered Number  {sum_num} is an Armstrong Number")
else:
    print("Eneterd number is not an Armstrong Number")


'''
⚡ Challenge Extension (Optional):

# Write a program that prints all Armstrong numbers in a given range.
# submit challenge answer links  here and tag me (use @Harikrishnan Mentor )
# '''

# x=int(input("Enter start of range:--"))
# y=int(input("Enter end of range:--"))
# print("Armstrong number between ",x ,"and",y ,"are:-")
# for i in range (x,y+1):
#     str_list=str(i)
#     sum_num_range=0
#     for j in range(0, len(str_list)):
#         sum_num_range+=int(str_list[j])**len(str_list)
#         if sum_num_range== i:
#             print(i,end=",")
#         else:
#             continue   