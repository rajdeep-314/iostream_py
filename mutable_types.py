def _dunder_methods(class_name, exclude = ['__new__', '__getattribute__', '__getnewargs__']):
    return [meth for meth in class_name.__dict__ if meth not in exclude]


class mutable_int():
    def __init__(self, arg=0):
        self._value = int(arg)

    for meth in _dunder_methods(int):
        cmd = f'''def {meth}func(self, *args):
            x = int.{meth}(self._value, *args)
            if x is NotImplemented:
                if '{meth}'[2] == 'r' and ('{meth}'[:2] + '{meth}'[3:]) in int.__dict__:
                    return type(args[0]).__{meth[2:]}(args[0], self._value)
                else:
                    return type(args[0]).__r{meth[2:]}(args[0], self._value)
            return x
        '''
        exec(cmd)
        exec(meth + ' = ' + meth + 'func')


# Only mutable_str is inheriting from str
# to work around the bug where syntax like
# 'x' + mutable_str('y') would not work
# Making mutable_int inherit from int or
# mutable_float inherit from float messes
# up a few considerable things.
class mutable_str(str):
    def __init__(self, arg=''):
        self._value = str(arg)

    for meth in _dunder_methods(str):
        # Non-r method
        cmd = f'''def {meth}func(self, *args):
            x = str.{meth}(self._value, *args)
            if x is NotImplemented:
                if '{meth}'[2] == 'r' and ('{meth}'[:2] + '{meth}'[3:]) in str.__dict__:
                    return type(args[0]).__{meth[2:]}(args[0], self._value)
                else:
                    return type(args[0]).__r{meth[2:]}(args[0], self._value)
            return x
        '''
        exec(cmd)
        exec(meth + ' = ' + meth + 'func')


class mutable_float():
    def __init__(self, arg=0.0):
        self._value = float(arg)

    for meth in _dunder_methods(float):
        # Non-r method
        cmd = f'''def {meth}func(self, *args):
            x = float.{meth}(self._value, *args)
            if x is NotImplemented:
                if '{meth}'[2] == 'r' and ('{meth}'[:2] + '{meth}'[3:]) in float.__dict__:
                    return type(args[0]).__{meth[2:]}(args[0], self._value)
                else:
                    return type(args[0]).__r{meth[2:]}(args[0], self._value)
            return x
        '''
        exec(cmd)
        exec(meth + ' = ' + meth + 'func')
