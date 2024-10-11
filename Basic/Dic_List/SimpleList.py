FirstList=[1,2,2,4,5,6,7,8]
for Number in FirstList: # simple for loop working over an array
    print('NUMBER ',Number)
    
print('Length Of An Array',len(FirstList)) # This is the length of an array
names=[]
for _ in range(3):
    names.append(input('Enter Name : '))
    
names=sorted(names)

print('Sorted Names : ',names)    
