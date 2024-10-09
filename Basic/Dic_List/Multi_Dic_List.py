#This is A List That Contains Multiple Dictionaries
students=[
    {'Name':'HAMZA','Full_Name':"Hamza Hussain",'Age':24,'Gender':'Male'},
    {'Name':'Bhatti','Full_Name':"Bhatti Hussain",'Age':27,'Gender':'Male'},
    {'Name':'ZA','Full_Name':"z Hussain",'Age':28,'Gender':'Male'},
    {'Name':'HA','Full_Name':"xy Hussain",'Age':29,'Gender':'Male'}
]

#Iterating through the list of dictionaries
for student in students:
    print(F'NAME : {student['Name']} | Age : {student['Age']} | Full Name : {student['Full_Name']}')