print "hello"
print "welcome to spychat"
print "let\'s get started"
spy_name=raw_input("what is your name ?  ")
if len(spy_name)>=3:
    print spy_name
    print "welcome " + spy_name + " ,glad to meet you"
    spy_salutation = raw_input("what should we call you(mr. or ms.)? ")
    if len(spy_salutation)>0:
        spy_name = spy_salutation +" "+ spy_name
        print "alright "  + spy_name+ "  i'd like to know you  little bit more"
        spy_age = input ("enter your age ")
        if spy_age>12 and spy_age<50:
            print ("your age fine to be a spy ")
            spy_rating =input("enter your spy_rating ")
            if spy_rating>= 5:
                print ("great spy")
            elif spy_rating>=4.5 and spy_rating<5:
                print "good spy"
            elif spy_rating>=3.5 and spy_rating<4.5:
                print "average spy"
            else:
                print("bad spy")
else:
    print "invalid name!!! please enter 3 letters name atleast"


