Amount=int(input('Enter How Many Sqaures To Be Printed : '))

# Simple Functioning Of A Multi Loop
for i in range(Amount):
    for j in range(Amount):
        print('#',end='')
    print()
    
# A Cleaner Version Of The Multi Loop
for i in range(Amount):
    print('#'*Amount)        
        