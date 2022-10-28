'''
  Name - Abhinav Tiwari



 Question :- Q1. Write a program to find all pairs of an integer array whose sum
          is equal to a given number?'''


#Solution :- 

lst=[5,6,4,2,7,3]
target_no=9
pair_array=[]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        sum=lst[i]+lst[j]
        if sum == target_no:
            pair_array.append([lst[i],lst[j]])       
print(pair_array)


#Output :- [[5, 4], [6, 3], [2, 7]]