import atexit as _atexit

# This one should implement buffers as well
class ostream:
    def __init__(self, has_buffer=True):
        if has_buffer:
            self._buffer = ''
        else:
            self._buffer = None

    def __lshift__(self, other):
        if type(other) == ostream_manipulator:
            other(self)
            return self

        if self._buffer is None:
            print(other, end = '')
        else:
            self._buffer += str(other)
        return self

    def flush(self):
        if not (self._buffer is None):
            print(self._buffer, end = '')
            self._buffer = ''


class ostream_manipulator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        self.func(*args)


def _endl_function(ostream_obj):
    ostream_obj << '\n'
    ostream_obj.flush()
    

cout = ostream()
cerr = ostream(has_buffer=False)
endl = ostream_manipulator(_endl_function)

def _exit_stream_flushing():
    cout.flush()

_atexit.register(_exit_stream_flushing)

# Demo
# cout << "Testing" << " things " << "out " << 1234
# cerr << "First expected output" << endl
# cout << endl
# cout << "Ok"
# cerr << "Yeah\n"
# cout << " then!"
# endl(cout)
# cout << "\nBuffer lalalalala\tlalalala"
# cout.flush()
