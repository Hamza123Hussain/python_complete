def main():
    print('hello')
    Student=New_Student()
    if(Student[0]=='a'):
        Student[1]='s'
    print(f'{Student[0]} Belong To {Student[1]}')
 
 
def New_Student():
     student=input('Enter Name : ')
     House=input('Enter House : ')
     return (student,House) # tuples are immutable meaning the value that is once set in them can not be chnaged 
 
 
 
 
 
 
 
 
if __name__=='__main__':
    main()    