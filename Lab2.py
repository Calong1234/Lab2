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
    print("the minimum temperature is " + str(minimum) + " and the maximum temperature is " + str(maximum))

def sort_temperature():
    inputt.sort()
    print(inputt)

def calc_median_temperature():
    length=len(inputt)
    if (len(inputt)%2==0):
        middle1=inputt[length//2]
        middle2=inputt[(length//2)-1]
        median=(middle1+middle2)/2
    else:
        median=inputt[length//2]
    print("the median temperature is " + str(median))


display_main_menu()
get_user_input()
calc_average()
find_min_max()
sort_temperature()
calc_median_temperature()