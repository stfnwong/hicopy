# Maybe just put everything here?

#from typing import List

atom = lambda x: not isinstance(x, list)
eq = lambda x, y: x == y

car = lambda x: x[0]
cdr = lambda x: x[1:]

cons = lambda x, y: [x, y] if atom(y) else [x] + y


#from pudb import set_trace; set_trace()
# Lisp eval - dumb name to avoid clash with python eval()
def leval(x):
    if atom(x):                 return x
    elif eq(car(x), "quote"):   return car(cdr(x))
    elif eq(car(x), "atom"):    return atom(eval(car(cdr(x))))
    elif eq(car(x), "eq"):      return eq(
        eval(car(cdr(x))),
        eval(car(cdr(cdr(x))))
    )
    elif eq(car(x), "car"):     return car(eval(car(cdr(x))))
    elif eq(car(x), "cdr"):     return cdr(eval(car(cdr(x))))
    elif eq(car(x), "cons"):    return cons(eval(car(cdr(x))), eval(car(cdr(cdr(x)))))
    elif eq(car(x), "cond"):
        for i in cdr(x):
            if eval(car(i)):
                return eval(car(cdr(i)))

    return []
