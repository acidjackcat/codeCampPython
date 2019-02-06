def testfunc(fname, lname):
    print('Привет, %s %s' % (fname, lname))

def testfunc(fname, lname):
    print('Привет, ' + str(fname) + str(lname))


testfunc('bob ', 'snow')

print(time.asctime())
