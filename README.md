# HOMOICONIC PYTHON

This is based on [this](https://aljamal.substack.com/p/homoiconic-python).

### Installation 
I am using `poetry` (version 1.82 at the time of writing) again which means I need to do this garbage with the keyring to get it to shut up. To install first silence poetry's nagging by doing

`export PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring`

so that each install doesn't harass you with keyring creation issues (if you hav a real keyring that you actually use then skip this step).


Then do

```
poetry install -v
```

or similar to install the environment. If you are letting poetry manage the environment then do something like

```
source $(poetry env info -p)/bin/activate 
```

### Lisp in Lisp
The whole of lisp is written in the Lisp Manual in terms of itself as 

```
eval[e;a] = [
    atom[e] -> assoc[e;a];
    atom[car[e]] -> [
        eq[car[e]; QUOTE] -> cadr[e];
        eq[car[e]; ATOM]   -> atom[eval[cadr[e]; a]];
        eq[car[e]; EQ]     -> [eval[cadr[e]; a] = eval[caddr[e]; a]];
        eq[car[e]; COND]   -> evcon[cdr[e]; a];
        eq[car[e]; CAR]    -> car[eval[cadr[e]; a]];
        eq[car[e]; CDR]    -> cdr[eval[cadr[e]; a]];
        eq[car[e]; CONS]   -> cons[eval[cadr[e]; a]; eval[caddr[e]; a]];
        T                  -> eval[cons[assoc[car[e]; a]; evlis[cdr[e]; a]]; a];
    ];
    eq[car[e]; LAMBDA]     -> 
        eval[caddr[e]; append[pair[cadar[e]; evlis[cdr[e]; a]; a]]]
]
