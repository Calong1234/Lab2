def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32):")

def get_user_input():
    input_list=input()
    input_list=input_list.split(", ")
    float_list=[float(i) for i in input_list]
    print(float_list)
    return float_list

def calc_average(x):
    average=sum(x)/len(x)
    print ("the average is " + str(average))
    return average

def find_min_max(x):
    minimum=min(x)
    maximum=max(x)
    min_and_max = [minimum, maximum]
    print("the minimum temperature is " + str(minimum) + " and the maximum temperature is " + str(maximum))
    return min_and_max

def sort_temperature(x):
    x.sort()
    print(x)
    return x

def calc_median_temperature(x):
    length=len(x)
    if (len(x)%2==0):
        middle1=x[length//2]
        middle2=x[(length//2)-1]
        median=(middle1+middle2)/2
    else:
        median=x[length//2]
    print("the median temperature is " + str(median))
    return median



if __name__ == "__main__":
    main()
