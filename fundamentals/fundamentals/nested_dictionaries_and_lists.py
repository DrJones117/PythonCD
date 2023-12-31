# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Challenge 1 -----

x[1][0] = 15
print(x)

# Challenge 2 -----

students[0]['last_name'] = 'Bryant'
print(students[0])

# Challenge 3 -----

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Challenge 4 -----

z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def iterateDictionary(x):
    for v in x:
        print(v)


iterateDictionary(students)

# Get Values From a List of Dictionaries

def iterateDictionary2(key, y):
    for dictionary in y:
        print(dictionary[key])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Iterate through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(x):
    print(len(x['locations']), x['locations'])
    print(len(x['instructors']), x['instructors'])


printInfo(dojo)