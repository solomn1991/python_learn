class MyException(Exception):
    def __init__(self,func,e):
        Exception.__init__(self)
        self.F = func
        self.E = e
    def __str__(self):
        return  "function "+self.F.__name__+" excetption:"+self.E.__str__()

def deal_exception(func):
    def decorated_func(*args,**kw):
        try:
            func(*args,**kw)
        except Exception,e:
            MyE = MyException(func,e)
            print MyE
            # raise MyE

    return decorated_func

@deal_exception
def calculate(x,y):
    print x/y


if __name__ == "__main__":
    calculate(5,0)

