print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32):")

def get_user_input():
    inpu=input()
    inpu=inpu.split(", ")
    global inputt
    inputt=[float(i) for i in inpu]
    print(inputt)

def calc_average():
    average=sum(inputt)/len(inputt)
    print ("the average is " + str(average))

def find_min_max():
    minimum=min(inputt)
    maximum=max(inputt)
    print("the minimum is " + str(minimum) + " and the maximum is " + str(maximum))

def sort_temperature():
    print(sort_temperature)

def calc_median_temperature():
    print(calc_median_temperature)


display_main_menu()
get_user_input()
calc_average()
find_min_max()