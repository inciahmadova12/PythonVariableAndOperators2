#task16
score=int(input())
if score<0 or score>100:
    print("No result")
else:
    result="pass" if score>51 else "fail"
    print(result)


#task17
order total=int(input())
membership=input("membership(yes or no):")
if order total<0 or (membership!=yes and membership!=no):
   print("delivery is rejected")
else:
    delivery fee=0 if order totlal>=50 or membership=="yes" else 5
    print(delivery fee)


#task18
day=int(input())
match day:
    case 1:
        print("monday,studyday")
    case 2:
        print("tuesday,studyday")
    case 3:
        print("wednesday,studyday")
    case 4:
        print("thursday,studyday")
    case 5:
        print("friday,studyday")
    case 6:
        print("saturday,weekend")
    case 7:
        print("sundat,weekend")
    case _:
        print("invaild day")


#task19
code=input()
quantity=int(input())
if quantity<1 or quantity>10:
    print("Invalid quantity")
else:
    match code:
        case "T":
            name="T"
            price=2
        case "C":
            name="Coffee" 
            price=4
        case "J":
            name="Juice"
            price=3
        case _:
            name="None"
            price=0
end=quantity*price
x="Large order" if son>=20 else "Regular order"
print(quantity,end,code,x)
