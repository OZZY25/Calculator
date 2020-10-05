# IMPORTANT VARIABLES
OP = ''
RES = 0
NUM1 = 0
NUM2 = 0
SUM_COUNT = 0
SUB_COUNT = 0
MULT_COUNT = 0
DIV_COUNT = 0

# FUNCTIONS
def number(num, data, data_LS, label):
    if len(data.get()) > 22:
        data_LS.set('')
        data_LS.set('OUT OF RANGE')
    else:
        data.set(data.get() + num)

# FUNCTION FOR ADDING 
def add(data):
    global OP
    global NUM1
    global RES 
    global SUM_COUNT

    OP = 'sum'
    if SUM_COUNT != 1:
        try:
            NUM1 = int(data.get())
        except ValueError:
            NUM1 = float(data.get())
        data.set('')
    else:
        NUM1 = RES
    SUM_COUNT += 1

# FUNCTION FOR SUBTRACTION
def sub(data):
    global OP
    global NUM1 
    global SUB_COUNT

    OP = 'sub'
    if SUB_COUNT != 1:
        try:
            NUM1 = int(data.get())
        except ValueError:
            NUM1 = float(data.get())
        data.set('')
    else:
        NUM1 = RES
    SUB_COUNT += 1

# FUNCTION FOR MULTIPLICATION
def mult(data):
    global OP
    global NUM1 
    global MULT_COUNT

    OP = 'mult'
    if MULT_COUNT != 1:
        try:
            NUM1 = int(data.get())
        except ValueError:
            NUM1 = float(data.get())
        data.set('')
    else:
        NUM1 = RES
    MULT_COUNT += 1

# FUNCTION FOR DIVISION
def div(data):
    global OP
    global NUM1 
    global DIV_COUNT

    OP = 'div'
    if DIV_COUNT != 1:
        try:
            NUM1 = int(data.get())
        except ValueError:
            NUM1 = float(data.get())
        data.set('')
    else:
        NUM1 = RES
        DIV_COUNT += 1

# SHOWING RESULTS
def result(data, data_LS):
    global RES
    global OP
    global NUM1
    global NUM2

    try:
        NUM2 = int(data.get())
    except ValueError:
        NUM2 = float(data.get())

    if OP == 'sum':
        RES = NUM1 + NUM2
    elif OP == 'sub':
        RES = NUM1 - NUM2
    elif OP == 'mult':
        RES = NUM1 * NUM2
    elif OP == 'div':
        try:
            RES = NUM1 / NUM2
        except  ZeroDivisionError:
            data_LS.set('')
            data_LS.set('ERROR')
    
    if RES != 0:
        data_LS.set(RES)
        data.set('')
    else:
        data.set('')

# DELETE ALL
def errase(data, data_LS):
    global OP
    global RES

    OP = ''
    RES = 0
    data.set('')
    data_LS.set('')
    
    # DELETE ONE NUMBER
def re(data, data_LS):
    new = data.get()
    data.set(new[:-1])
    data_LS.set(new[:-1])