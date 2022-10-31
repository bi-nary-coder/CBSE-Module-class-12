'''
Project question -Create a binary file with name and roll number. Search for a given roll
                  number and display the name, if not found display appropriate
                  message. 
'''
# Solution:-
f=open('student marks.dat', 'wb')
n=int(input("enter the total number of names"))
c=0
for i in range(n):
    roll=str(input("Enter the roll number")+"\n")
    name=str(input("Enter the name")+"\n")
    f.write(roll.encode("utf-8"))
    f.write(name.encode("utf-8"))
f.close()
f=open('student marks.dat', 'rb')
data=f.readlines()
print (data)
roll=str(input("enter the roll number you want to find")+'\n')
for i in data:
    if i.decode('utf-8')==roll:
        c=c+1
if c==1:
   print('Name=',(data[data.index(roll.encode("UTF-8"))+1].decode('utf-8')))
else:
    print(roll,"not found")
f.close()