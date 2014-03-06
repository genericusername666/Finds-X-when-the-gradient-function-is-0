def equation(x):
    #DEAR USER
    #ENTER YOUR EQUATION HERE: (bracket everything)
    return (x**3)+(2*(x**2))+(3*x)
#Code by Ralph Richards 06/mar/2014
def menu():
    global degreeofaccuracy
    global decrease
    print("Ensure your equation has been plugged into the program file")
    degreetrue=False
    while not degreetrue:
        degreeofaccuracy=input("Enter your degree of accuracy (can't be 0) (smaller numbers = longer working times) (e.g. 0.0001) \nDegree of accuracy: ")
        if float(degreeofaccuracy)!=0:
            degreeofaccuracy=float(degreeofaccuracy)
            degreetrue=True
    decreasetrue=False
    while not decreasetrue:
        decrease=input("Enter the decrease number (can't be 0) (smaller decrease = more accurate results) (smaller decrease = longer working times) (e.g. 0.01) \nDecrease: ")
        if float(decrease)!=0:
            decrease=float(decrease)
            decreasetrue=True
menu()
found=False
ci=1
cii=2
print("Working on it!")
while not found:
    #print("loop")
    #print("ci "+str(ci))
    #print("cii "+str(cii))
    #print("ci returns "+str(equation(ci)))
    #print("cii returns "+str(equation(cii)))
    if -degreeofaccuracy<equation(cii) and equation(cii)<degreeofaccuracy:
        print("\n\ntrue")
        print("X = "+str(cii))
        print("returns "+str(equation(cii)))
    if -degreeofaccuracy<equation(ci) and equation(ci)<degreeofaccuracy:
        print("\n\ntrue")
        print("X = "+str(cii))
        print("returns "+str(equation(cii)))
        found=True
    if equation(ci)>0:
        if equation(cii)<equation(ci):
            if equation(cii)!=0:
                ci-=decrease
                cii-=decrease
            else:
                print("error")
        else:
            cii=ci
            ci-=decrease
    elif equation(ci)<0:
        if equation(cii)<equation(ci):
            if equation(ci)!=0:
                ci-=decrease
                cii-=decrease
            else:
                print("error")
print("\n\nYou're welcome")
