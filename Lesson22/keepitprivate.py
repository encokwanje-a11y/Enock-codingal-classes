class myClass:


    __privateVar = 27;
     

    def __priveMeth(self):
        print("I'm inside a class myClass")

    def hello(self):
        print("Private Variable value: ", myClass.__privateVar) 

foo = myClass()
foo.hello()
foo.__privMeth