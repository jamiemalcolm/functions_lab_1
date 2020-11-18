def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2
def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

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
    #reversed_string = a.reversed()
    #return reversed_string
    return a[::-1]

def temp_converter(degree):
    return (degree - 32) * 5/9