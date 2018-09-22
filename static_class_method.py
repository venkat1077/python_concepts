class classA(object):

    val1 = 10

    def __init__(self, val2):
        self.val2 = val2
        
    @staticmethod
    def func1():
        print "Inside static method"

    @staticmethod
    def func2():
        #Creating objects for classA inside static method - can not use instance inside
        return classA(10)

    @classmethod
    def func3(cls):
        print "Inside class method"
        #Accessing class attributes using cls(class name)
        print cls.val1
        #Creating objects using cls(class name)
        obj = cls(cls.val1 + 1)
        print obj.val2

    @classmethod
    def func4(cls):
        obj = cls(cls.val1 + 10)
        return obj

#calling static method without creating instance
classA.func1()

#Using static method to create & return the objects
obj1 = classA.func2()
print obj1

#calling class method without creating instance
classA.func3()

#Using class method to create & return the objects
obj2 = classA.func4()
print obj2
