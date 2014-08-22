__author__ = 'chenliang'

def co(fun):
    def start(*args, **kwargs):
        print "Calling decorator with args=", str(*args), " kwargs=", str(**kwargs)
        cr = fun(*args, **kwargs)
        cr.next()
        return cr
    return start

@co
def grep(p):
    print "Calling grep with pattehr -> ", p
    while True:
        line = yield
        if p in line:
            print "Bingo -> ", line
        else:
            print "Noooooooooooo"

# g = grep("test")
# g.send("just a test")
# g.send("whatever")
# g.close()

def grep2(p):
    print "Calling grep with pattehr -> ", p
    while True:
        line = yield
        if p in line:
            print "Bingo -> ", line
        else:
            print "Noooooooooooo"

g = grep2("test")
g.next()
# g.send(None)
g.send("is there a test?")