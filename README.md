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
