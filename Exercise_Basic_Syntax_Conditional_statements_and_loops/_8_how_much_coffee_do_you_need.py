command = input()
lower_case_event_list = ['coding', 'dog', 'cat', 'movie']
upper_case_event_list = ['CODING', 'DOG', 'CAT', 'MOVIE']
number_of_coffees = 0

while command != 'END':
    if command in lower_case_event_list:
        number_of_coffees += 1
    if command in upper_case_event_list:
        number_of_coffees += 2
    if number_of_coffees > 5:
        print('You need extra sleep')
        break
    command = input()
else:
    print(number_of_coffees)
