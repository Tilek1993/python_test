empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

another_empty_list = list()
another_empty_list
[]

list('cat')
['c','a','t']

a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)
['ready','fire','aim']

birthday = '1/6/1952'
birthday.split('/')
['1', '6', '1952']

splime = 'a/b//c/d///e'
splime.split('/')
['a', 'b', '', 'c', 'd', '', '', 'e']

splime = 'a/b//c/d///e'
splime.split('/')
['a/b', 'c/d', '/e']

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]
'Groucho'
marxes[1]
'Chico'
marxes[2]
'Harpo'

marxes[-1]
'Harpo'
marxes[-2]
'Chico'
marxes[-3]
'Groucho'

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
all_birds
[['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], 'macaw', [3, 'French hens', 2, 'turtledoves']]

all_birds[0]
['hummingbird', 'finch']
all_birds[1]
['dodo', 'passenger pigeon', 'Norwegian Blue']
all_birds[1][0]
'dodo'