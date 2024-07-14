# iostream

The repository needs some tiding up and a good README file, but for now, this should do.

## Note

I've fixed the `mutable_tpyes` now, for the most part (only one bug found so far). I'm not using a metaclass anymore, as I was overcomplicating it. I will probably condense the three class definitions in `mutable_types.py` to three calls to a single function, the function serving as a template, of sorts.

The stuff that follows is no longer entirely relevant to the current state of the repository, but it has some important points that I want to incorporate into the final README, so I'm still leaving it here. Feel free to go through it :)

For a proper demo of the facilities provided across the modules, check out `iostream_demo.py`

<hr>

I wanted to make syntax similar to C++'s standard I/O operations work in Python. For example:
```python
from iostream_py import *

cout << "Hello, World!" << endl
```

should print `Hello, World!` to the console. <br>

That, in itself is quite easy, just create an `ostream` class for instantiating `cout`, `cerr` and `clog`. Then define a `__lshift__` to make `<<` usable. Implement a buffer for those ostream objects that require it (namely, `cout` and `clog` here). And then, make another class for the function-esque `ostream_manipulators`, such as `endl`, for which executing `ostream_obj << ostream_manipulator` would execute `ostream_manipulator(ostream_obj)`, and return `ostream_obj`.

By the way, the following works in C++
```c++
#include <iostream>

int main() {
    std::cout << "Hi";
    std::endl(std::cout);
    std::cout << "There";
}
```

The three lines inside `main` do the same thing that a single `std::cout << "Hi" << std::endl << "There";` does, but the point is that `std::endl` is a function in C++, which is why my `endl` is one too. <br>

The tricky part is implementing `cin`. Consider the following code
```c++
#include <iostream>

int main() {
    int a;
    std::cin >> a;
    std::cout << "Twice of a is " << 2*a;
}
```
How the stuff inside `main` works in C++ is, `a` is declared to be an integer inside `main`'s scope. An unqualified lookup for the namespace `std` occurs and then a qualified lookup inside it for the `istream` object `cin`. Then, the `<<` operator's overloading is resolved for the second operand being an `int` object, and then the user is allowed to type something into `cin`, which is then processed accordingly to extract an `int`. Then, the twice of that is simply printed to `cout`.

Coming up with such a syntax for Python is challenging, though. You can't do something like
```python
a = int()
cin >> a
```
This is because integers are immutable in Python. They don't even have a `__init__` method, just a `__new__` method that creates them. The same goes for `str` and `float` classes, for example, the instances of both being immutable.

My workaround for this was to create my own classes for mutable types of traditionally immutable ones. These would inherit from the immutable types, store the data in an attribute and all methods will be mapped to operate on the attribute rather than the instance. Then, `cin` could just alter the attributes of these objects. So, the following syntax would work

```python
x = mutable_int()
cin >> x
cout << "Twice of x is " << (2*x)
```

And it does work.

However, the mutable classes are a long way from perfect. I keep encountering unexpected bugs wherein the mutable instances don't interact well with the builtin classes. For example, the following code won't work
```python
x = mutable_int(10)
y = 'abcd'

print(x*y, y*x, sep = "\n")          # One of these (sometimes both) usually doesn't work
```

But the following does work
```python
x = mutable_int(10)
y = mutable_str('abcd')

print(x*y, y*x, sep = "\n")
```

Why the disparity? I don't know yet.

<hr>

Also, I've made it such that if you do something like this
```python
a = mutable_int()

cin >> a
```

and you repeatedly keep pressing RETURN or typing spaces, the program will simply keep prompting you to enter something meaningful. If after all that, you enter an integer, followed by whatever you want, it'll extract the integer, keeping the rest stored in a buffer. If you enter something starting with stuff that cannot be interpreted as an integer (say you enter 'abcd', for example), it will just extract 0. This is how it works in C++ as well.
Maybe these problems would be a little easier to debug as well, if I hadn't resorted to using a metaclass. The latest versions of `mutable_int`, `mutable_str` and `mutable_float` are all instances of the metaclass `_mutable_meta`, which gives each of these classes an `__init__` method that stores the required value in an attribute named `value`, and then redirects other dunder methods. For example, `mutable_int.__add__(x, y)` just returns `int.__add__(x.value, y)`. But there are problems when methods like `__radd__` or `__rmul__` are being called. I don't know why (yet).

<hr>

Anyway, I've dumped the code here, and I'll work on it soon, hopefully.
