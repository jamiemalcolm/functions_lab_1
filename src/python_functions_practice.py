def return_10():
    return 10

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    return int(a) + int(b)



months = {  1: {
            "short_name": "Jan",
            "month": "January",},
            3: {
            "short_name" : "Mar", 
            "month" : "March"},
            9: {
             "short_name": "Sep",
            "month": "September"},
            4:{
             "short_name": "Apr", 
             "month" : "April"},
            10:{
             "short_name": "Oct", 
            "month": "October"}
}

def number_to_full_month_name( a ):
    return months[a]["month"]


def number_to_short_month_name( a ):
    return months[a]["short_name"]


def find_volume( a ):
    return a ** 3

def reversed_string(a):
    return a[::-1]
   