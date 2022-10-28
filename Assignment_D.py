'''

Name = Abhinav Tiwari

Question :- Q4. Write a program to print the first non-repeated character from a string?'''


#Solution :- 


string_=input("Enter a string :- ")
#string_="aagcdefccb"
count=0
d={}
for i in range(len(string_)):
    if string_[i] in d.keys():
        continue
    for j in range(i+1,len(string_),1):
        if string_[i] == string_[j]:
            #print("yes",str[j])
            count+=1
    d[string_[i]]=count
    count=0

for i in d:
    if d[i]==0:
        print("First Non-repeated value is :-",i)
        break
    
print(d)
