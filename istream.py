from ostream import *
from mutable_types import *


class istream:
    def __init__(self):
        self.buffer = ''

    def __rshift__(self, other):
        cout.flush()
        if type(other) == mutable_int:
            other._value = self.extract_int()
        elif type(other) == mutable_str:
            other._value = self.extract_str()
        elif type(other) == mutable_float:
            other._value = self.extract_float()
        else:
            raise TypeError("Type not recognized by cin")
        return self

    def open_stream(self):
        while self.buffer == ' '*len(self.buffer):
            self.buffer = input()

    def handle_leading_spaces(self):
        i = 0
        while i < len(self.buffer):
            if self.buffer[i] == ' ':
                i += 1
            else:
                break
        self.buffer = self.buffer[i:]

    def extract_str(self):
        self.open_stream()
        self.handle_leading_spaces()
        temp = ''
        i = 0
        while i < len(self.buffer):
            if self.buffer[i] != ' ':
                temp += self.buffer[i]
                i += 1
            else:
                break
        
        self.buffer = self.buffer[i:]
        return temp

    def extract_int(self):
        self.open_stream()
        self.handle_leading_spaces()
        temp = ''
        i = 0
        while i < len(self.buffer):
            if self.buffer[i].isdigit():
                temp += self.buffer[i]
                i += 1
            else:
                break
        
        self.buffer = self.buffer[i:]
        return int(bool(temp) and int(temp))
        

cin = istream()
