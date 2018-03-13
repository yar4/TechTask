s= input()
def string_handler(s):
    numbers = 0
    letters = 0
    for i in s:
        while True:
            try:
                if i.isdigit()is True:
                    numbers+=1
                break
            except Exception as e:
                print(e)
        try:
            if i.isalpha() is True:
                letters+=1
        except Exception as e:
            print(e)
    return (numbers,letters)
print(string_handler(s))





