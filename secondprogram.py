# user input that multiply a list of numbers from waht the user is inputting (multiplication table) between 1 - 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
table = list(map(lambda x : x * 5, numbers))
print(table)