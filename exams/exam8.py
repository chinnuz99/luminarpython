# when is the finally block executed.Explain with example?
a=int(input("enter"))
b=int(input("enter"))
try:
    print("hello")
    print(a/b)
except:
    print("exception")
finally:
    print("inside finally")

#try block is executed every time.
#except work in exceptions
#finally work every time
