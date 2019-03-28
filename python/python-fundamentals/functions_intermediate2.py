# 1. Given x = [ [5,2,3], [10,8,9] ] How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
def changeValue (list):
    list[1:0]=15
    print (list)

changeValue ([[5,2,3], [10,8,9]])


# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students = {'first_name': ['Michael', 'John'], 'last_name' : ['Jordan', 'Rosales']}

def changeName ():
    for i in range(len(students['first_name'])):
        students['last_name'][0]='Bryant'
        print (students['first_name'][i], students['last_name'][i]) 

changeName ()


# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

def changeSports ():
    sports_directory['soccer']=['Andres', 'Ronaldo', 'Rooney']
    print (sports_directory['soccer'])

changeSports () 


# For z, how would you change the value 20 to 30? z = [ {'x': 10, 'y': 20} ]
def changeZ ():
    z = {'x': 10, 'y': 20}
    z['y']=30
    print (z)

changeZ ()


# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
# iterateDictionary( students ) should output:
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def iterateDictionary ():

    students = {'first_name': ['Michael', 'John', 'Mark', 'KB'], 'last_name' : ['Jordan', 'Rosales', 'Guillen', 'Tonel']}
    for i in range(len(students['first_name'])):
        print ('first_name', students['first_name'][i], ',', 'last_name', students['last_name'][i])

iterateDictionary () 


#iterateDictionary v2:
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary (student_list):    
    for student in student_list:
        print ("first_name", student['first_name'],",", "last_name", student['last_name'])

iterateDictionary(students)


# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
def interateDictionary2 (): 

    students = {'first_name': ['Michael', 'John', 'Mark', 'KB'], 'last_name' : ['Jordan', 'Rosales', 'Guillen', 'Tonel']}
    for i in range(len(students['first_name'])):
        print (students['first_name'][i])

iterateDictionary2 ()


# 4. Say that
# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
def printDojoInfo ():

    dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
    print (len(dojo['locations']), "LOCATIONS")
    for i in range(len(dojo['locations'])):
        print (dojo['locations'][i])

printDojoInfo ()


# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
def printDojoInst ():

dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
print (len(dojo['instructors']), "INSTRUCTORS")
for i in range(len(dojo['instructors'])):
    print (dojo['instructors'][i])

printDojoInst ()