
def leap(year):
    #year = input("Input the year you want to check: ")
    #print(year)
    if(int(year)% 4 == 0):
        if(int(year)%100 ==0):
            if(int(year)% 400 == 0):
                return 'This is a leap year'
            else: 
                return 'not a leap year'
        else: 
            return 'This is a leap year'
    else: 
        return 'not a leap year'