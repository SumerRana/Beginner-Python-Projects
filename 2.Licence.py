age=int(input("Please input your age: "))

# if age < 18:
#     if age <=10:
#         print("paida hote hi aa gya check krne")
#     else:
#     	print("not eligible")
# elif age == 18:
#     print("ohho ho gye 18 k, aajao")
# elif age < 70:
#     print("eligible and fit age")
# elif age == 70:
#     print("chla lo or bs yhi saal hai")
# else:
#     print("chacha rest kr lijiye nhi to rest in peace ho jayenge")
if age >0:
    if age<=70:
        if age!=70:
            if age!=18:
                if age<18:
                    if age<=10:
                        print("paida hote hi aa gya check krne")
                    else:
                        print("not eligible")
                else:
                    print("eligible and fit age")
            else:
                print("ohho ho gye 18 k, aajao")
        else:
            print("chla lo or bs yhi saal hai")
    else:
        print("chacha rest kr lijiye nhi to rest in peace ho jayenge")
else:
    print("error")

