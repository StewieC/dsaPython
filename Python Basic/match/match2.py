# use underscore as the last case if you want the code to execute when there are no other matches

day = 10
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
        
        # pipe character | is used to match multiple values`
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day") # default case
        
    
# if statements as guards

month = 5
day = 4

match day:
    
    case 1 | 2 | 3 | 4 | 5 if month:
        print("a weekend in april")
        
    case 1 | 2| 3 | 4 | 5  if month == 5:
        print("Second week")
   