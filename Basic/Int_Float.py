# CONVERTING STRING TO A NUMBER AND THEN ADDING THEM UP
Number=int(input('Enter Number 1  : '))
Number2=int(input('Enter Number 2 : '))
print(f"THE SUM OF BOTH : {Number+Number2}")

#converting num 1 to float. the sum would come in float format as it has higher precedence
Number=float(input('Enter Number 1  : '))
Number2=int(input('Enter Number 2 : '))
print(f"THE SUM OF BOTH : {Number+Number2}")

#Rounding off a number
print(f"ROUND OFF NUMBER : {round((Number))}")

#specifying a seperator that comes after or before the value
print(f"THE SUM OF BOTH : {Number+Number2:.4f}") #here we are specifying that we nedd 4 decimal place in the answer
