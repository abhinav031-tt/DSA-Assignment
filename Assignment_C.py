Question :- Q3. Write a program to check if two strings are a rotation of each other?'''

#Solution :- 

string_1=input("Enter a string 1 :- ")
string_2=input("Enter a string 2 :- ")
if len(string_1) == len(string_2):
    temp=string_1+string_1
    if string_2 in temp:
        print("Rotation")
    else :
        print("No Rotation")
else :
    print("No Rotation ")
