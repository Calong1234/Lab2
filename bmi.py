def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/height/height
    print ("bmi = " + str(bmi))
    if(bmi<18.5):
        print ("Underweight")
        return -1
    elif(bmi>25):
        print ("Overweight")
        return 1
    else:
        print ("Normal Weight")
        return 0
calculate_bmi(weight=5.7, height=1.73)