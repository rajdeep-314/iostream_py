# Only int, str and float, for now. They are immutable and have no __init__

# Returns a list of dunder method names from class_name, except if they are in exclude
def dunder_methods(class_name, exclude = ('__new__', '__getattribute__')):
    return [meth for meth in class_name.__dict__ if meth.startswith('__') and meth.endswith('__') and meth not in exclude]

class mutable_int(int):
    def __init__(self, arg=0):
        self.value = arg

    for meth in dunder_methods(int):
        exec(meth + '= lambda self, *args : int.' + meth + '(self.value, *args)')

    del(meth)


class mutable_str(str):
    def __init__(self, arg=''):
        self.value = arg

    for meth in dunder_methods(str):
        exec(meth + '= lambda self, *args : str.' + meth + '(self.value, *args)')

    del(meth)


class mutable_float(float):
    def __init__(self, arg=0.0):
        self.value = arg

    for meth in dunder_methods(float):
        exec(meth + '= lambda self, *args : float.' + meth + '(self.value, *args)')

    del(meth)
