# -*- coding:utf-8 -*-


class Character:
    def __init__(self, ch):
        self.code = ord(ch)
        self.ch = ch

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.code == other.code and self.ch == other.ch

    def isA(self, c):
        return self.code == c or self.ch == c

    @property
    def isEOF(self):
        # eof = "\0"
        return self.code == 0x00

    @property
    def isLetter(self):
        # letter = "A" .. "Z" | "a" .. "z"
        return (self.code >= 0x41 and self.code <= 0x5a) or \
            (self.code >= 0x61 and self.code <= 0x7a)

    @property
    def isDecimalDigit(self):
        # decimalDigit = "0" .. "9"
        return self.code >= 0x30 and self.code <= 0x39

    @property
    def isOctalDigit(self):
        # octalDigit = "0" .. "7"
        return self.code >= 0x30 and self.code <= 0x37

    @property
    def isHexDigit(self):
        # hexDigit = "0" .. "9" | "A" .. "F" | "a" .. "f"
        return (self.code >= 0x30 and self.code <= 0x39) or \
            (self.code >= 0x41 and self.code <= 0x46) or \
            (self.code >= 0x61 and self.code <= 0x66)

    @property
    def isWhitespace(self):
        # Whitespace = " " | "\t" | "\r" | "\n"
        return self.code == 0x20 or self.code == 0x09 or \
            self.code == 0x0d or self.code == 0x0a
