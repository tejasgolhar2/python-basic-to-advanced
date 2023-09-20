# Nesting List inside Dictionary
# --->>> the list inside the dictionary is accessed by using the key values

languages = {
    "tejas": ['Marathi','English','Sanskrit','Hindi'],
    "neha":['Telugu','Outer Space'],
    "sakshi": ['Cant speak']
}
print(languages['sakshi'])


# Nesting Dictionary inside Dictionary
# --->>> the dictionary inside the dictionary is accessed by using the key values

languages1 = {
    "tejas": { 'favourites': ['Marathi','English','Sanskrit','Hindi'],
              'experience': 11 
              },
    "neha":{'favourites':['Telugu','Outer Space'],
            'experience':21
            },
    "sakshi": ['Cant speak']
}


# Nesting Dictionary inside List
#   ---->>> the dictionary as element of the list is accessed by using index values

languages2 = [
    {   'username': "tejas",
        'favourites': ['Marathi','English','Sanskrit','Hindi'],
        'experience': 11 
    },
    {   'username': "neha",
        'favourites': ['Telugu','Outer Space'],
        'experience': 21 
    },
    {   'username': "sakshi",
        'favourites':['Cant speak'],
        'experience': 20
    }   
]
