while True:
    a=input("loginni kiriting: ")
    b=int(input("parolni kiriting: "))
    c=input("tug'ilgan sanani kiriting: ")
    if a=="madijon" and b==12345 and c=="13.03.04":
        print("dasturga kirdingiz")
        break
    elif a=="madijon" and c=="13.03.04":
        print("parol xato")
    elif b==12345 and c=="13.03.04":
        print("login xato")
    elif a=="madijon" and b==12345:
        print("tug'ilgan sana xato")
    elif a=="madijon":
        print("parol bn sana xato") 
    elif b==12345 :
        print("lobin bn sana xato") 
    elif c=="13.03.04":
        print("login bn parol xato")

    else:
        print(" Login ,parol va tug'ilgan sana  xato")
            
