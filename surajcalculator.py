from re import A


def su_cal():
    print("<<<<<<SURAJ CALCULATOR>>>>>>")
    print("")
    print("1.ADDITION (+)")
    print("")
    print("2.SUBTRACTION(-)")
    print("")
    print("3.Multiplication (*)")
    print("")
    print("4.Division (/)")
    print("")
    a = int(input("enter no : "))
    print("")
    if a == 1:
        print("ADDITION (+)")
        print("")
        add1 = int(input("enter 1 value :"))
        add2 = int(input("enter 2 value :"))
        add3 = add1 + add2
        print("YOUR ANSWER IS = " + str(add3))

    elif a == 2:
      print("SUBTRACTION (-)")
      print("")
      add4 = int(input("enter 1 value :"))
      add5 = int(input("enter 2 value :"))
      add6 = add4 - add5
      print("YOUR ANSWER IS = " + str(add6))


    elif a == 3:
      print("Multiplication (*)")
      print("")
      add7 = int(input("enter 1 value :"))
      add8 = int(input("enter 2 value :"))
      add9 = add7 * add8
      print("YOUR ANSWER IS = " + str(add9))
    elif a == 4:
      print("Division (/)")
      print("")
      add10 = int(input("enter 1 value :"))
      add11 = int(input("enter 2 value :"))
      add12 = add10 / add11
      print("YOUR ANSWER IS = " + str(add12))
    else:
      print("failed to identify")

su_cal()

