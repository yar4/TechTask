number1= int(input())
number2= int(input())
number3= int(input())

def handle_number(number1,number2,number3):#function takes 3 arguments
    division = list(range(number1,number2))#convert to list
    counting = 0#score counter
    for result in division[:]:
        a = result % number3 #we find division without rest
        try:
            if a == 0:
                counting+=1#set score
        except:
            print('Incorect input')
    return counting
print(handle_number(number1,number2,number3))



















