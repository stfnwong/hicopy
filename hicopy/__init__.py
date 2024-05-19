# Basic operations 

atom = lambda x: not isinstance(x, list)
eq = lambda x, y: x == y

car = lambda x: x[0]
cdr = lambda x: x[1:]

cons = lambda x, y: [x, y] if atom(y) else [x] + y


# Lisp leval - dumb name to avoid clash with python eval()
def leval(x):
    if atom(x):                 return x
    elif eq(car(x), "quote"):   return car(cdr(x))
    elif eq(car(x), "atom"):    return atom(leval(car(cdr(x))))
    elif eq(car(x), "eq"):      return eq(
        leval(car(cdr(x))),
        leval(car(cdr(cdr(x))))
    )
    elif eq(car(x), "car"):     return car(leval(car(cdr(x))))
    elif eq(car(x), "cdr"):     return cdr(leval(car(cdr(x))))
    elif eq(car(x), "cons"):    return cons(leval(car(cdr(x))), leval(car(cdr(cdr(x)))))
    elif eq(car(x), "cond"):
        for i in cdr(x):
            if leval(car(i)):
                return leval(car(cdr(i)))

    return []
