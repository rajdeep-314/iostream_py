# Metaclass for making mutable type classes
class _mutable_meta(type):
    __cache__ = set()

    # Returns a list of dunder method names from class_name, except if they are in exclude
    def dunder_methods(class_name, exclude = ('__new__', '__getattribute__', '__init__')):
        return [meth for meth in eval(class_name + '.__dict__') if meth.startswith('__') and meth.endswith('__') and meth not in exclude]

    # Generates a function to be used as 
    # __init__ for type_name
    # This function assigns the argument passed
    # during initialization to a "value" attribute
    # The default arguments are based on type_name
    # eg : 0 for int, 0.0 for float, '' for str
    def init_function_generator(type_name):
        def init_function(self, arg = eval(type_name + '()')):
            self.value = eval(type_name)(arg)
        return init_function
    
    # class_name format : mutable_<type_name>
    # eg : mutable_int, mutable_str, mutable_float
    def __new__(cls, class_name, bases, attributes):
        type_name = class_name[8:]              # eg : extracts int from mutable_int, str from mutable_str
        bases = (eval(type_name),)              # to make the mutable classes an instance of the actual ones

        # __init__ method
        attributes['__init__'] = cls.init_function_generator(type_name)

        # other usual dunder methods
        for meth in cls.dunder_methods(type_name):
            # Hack cus I can't figure out an alternative, for now
            cmd = f'''def {meth}_func(self, *args):
                new_args = []
                for arg in args:
                    if type(arg) in self.__class__.__cache__:
                        new_args.append(type(arg)._actual_class(arg))
                    else:
                        new_args.append(arg)
                return {type_name}.{meth}(self.value, *new_args)
            '''

            exec(cmd)
            attributes[meth] = eval(meth + '_func')
            
            # Previously :
            # attributes[meth] = eval('lambda self, *args : ' + type_name + '.' + meth + '(self.value, *args)')

        instance = super().__new__(cls, class_name, bases, attributes)
        cls.__cache__.add(instance)
        return instance
    
    def __init__(self, class_name, bases, attributes):
        self._type_name = class_name[8:]
        self._actual_class = eval(self._type_name)        # eg : int for mutable_int

    def __str__(self):
        return 'mutable_' + self._type_name


# The following mutable types have been defined here
class mutable_int(metaclass = _mutable_meta): pass
class mutable_str(metaclass = _mutable_meta): pass
class mutable_float(metaclass = _mutable_meta): pass
