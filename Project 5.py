'''
Project question - Removes all the line that contains character 'a' in a file
                              and write it to another file.
'''
# solution:-
file1=open("inputfile.txt",'r+')
data1=file1.readlines()
file1.close()
file1=open("inputfile.txt",'w')
data2=[]
file2=open("outputfile.txt",'w')
data3=[]
for i in data1:
        if "a"in i:
            data3=data3+[i]
        else:
            data2=data2+[i]
file1.writelines(data2)
file2.writelines(data3)
file1.close()
file2.close()