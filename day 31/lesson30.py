def simple_calculator(num1, num2, operation):
    if operation == "damateba":
        return num1 + num2
    elif operation == "gamokleba":
        return num1 - num2
    elif operation == "gamravleba":
        return num1 * num2
    elif operation == "gaxoba":
        if num2 == 0:
            return "chechdoba: nulze gaxoba ceujlebelia"
        else:
            return num1 / num2
    else:
        return "shecdom: uchnobi oberachia"



#2

def calculate_area(length, width): 
    return length * width

length = 5
width = 10
area = calculate_area(length, width)
print(f"partobi aris: {area}")


#3

def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2