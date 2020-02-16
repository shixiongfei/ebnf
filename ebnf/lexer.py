# -*- coding:utf-8 -*-

from .exception import SyntaxException
from .character import Character


class Token:
    RULE = 1
    LITERAL = 2
    SYMBOL = 3

    def __init__(self, token, tag):
        self.token = token
        self.tag = tag

    def asString(self):
        return "<{0}:{1}>".format(self.token, self.tag)

    def __repl__(self):
        return self.asString()

    def __str__(self):
        return self.asString()


class Lexer:
    def __init__(self, source):
        self.source = source
        self.current = Character(' ')
        self.index = -1
        self.line = 1
        self.column = 1

    def nextChar(self):
        try:
            self.current = Character(self.source[self.index + 1])
            self.index = self.index + 1
            self.column = self.column + 1
        except IndexError:
            self.current = Character('\0')
        return self

    def skipWhitespace(self):
        while self.current.isWhitespace:
            if self.current.isA('\n'):
                self.line = self.line + 1
                self.column = 0
            self.nextChar()
        return self

    def readLiteral(self):
        quotation = self.current
        word = []

        while True:
            self.nextChar()

            if self.current.isA('\\'):
                self.nextChar()

                if self.current.isA('t'):
                    ch = '\t'
                elif self.current.isA('r'):
                    ch = '\r'
                elif self.current.isA('n'):
                    ch = '\n'
                else:
                    ch = self.current.ch

                word.append(ch)
                self.nextChar()

            if self.current == quotation:
                self.nextChar()
                break

            if self.current.isEOF:
                raise SyntaxException("Unexpect end of file")

            word.append(self.current.ch)

        return Token("".join(word), Token.LITERAL)

    def readRule(self):
        word = []

        while self.current.isLetter or \
                self.current.isDecimalDigit or \
                self.current.isA('_'):
            word.append(self.current.ch)
            self.nextChar()

        return Token("".join(word), Token.RULE)

    def readSymbol(self):
        token = Token(self.current.ch, Token.SYMBOL)
        self.current = Character(' ')
        return token

    def scan(self):
        self.skipWhitespace()

        if self.current.isEOF:
            self.current = Character(' ')
            return None

        if self.current.isA('"') or self.current.isA("'"):
            return self.readLiteral()

        if self.current.isLetter:
            return self.readRule()

        return self.readSymbol()
