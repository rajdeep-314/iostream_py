from iostream import *

# The classic
cout << "Hello, World!" << endl


cout << "\nDemo 1 ->" << endl
# ostream and buffer demo
cout << "Testing" << " things " << "out " << 1234
cerr << "First expected output" << endl
cout << endl
cout << "Ok"
cerr << "Yeah\n"
cout << " then!"
endl(cout)
cout << "\nBuffer - gonna be flushed soon"
cout.flush()
cout << endl


cout << "\nDemo 2 ->" << endl
# istream (cin, specifically) demo
cout << "Enter a positive integer, followed by a string\n"
a = mutable_int()
b = mutable_str()
cin >> a >> b
cout << (a*b) << " should be the same as " << (b*a) << "\n"


cout << "\nDemo 3 ->" << endl
# more cin demo
a = mutable_int()
b = mutable_int()
c = mutable_int()

cout << "Enter 3 integers, up to you to enter them at once, or one by one" << endl << "As soon as the program receives two of them"
cout << ", it will evaluate and print their sum, and will wait for the third one, if it hasn't been extracted already" << endl
cin >> a >> b
cout << "Currently a + b is " << (a+b) << endl
cin >> c
cout << "a + b + c = " << (a+b+c)
