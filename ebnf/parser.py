# -*- coding:utf-8 -*-

import logging
from .exception import SyntaxException
from .lexer import Token
from .primitives import Rule, \
    Optional, Repetition, Grouping, Alternation, Concatenation

logger = logging.getLogger('remrpc')


class Parser:
    EQUALS = Token('=', Token.SYMBOL)
    SEMICOLON = Token(';', Token.SYMBOL)

    def __init__(self, lexer):
        self.lexer = lexer
        self.look = None
        self.moveNext()

    def error(self, message):
        logger.error(self.lexer.source.split('\n')[self.lexer.line - 1])
        logger.error("{0}^".format(" " * (self.lexer.column - 1)))
        raise SyntaxException(message)

    def moveNext(self):
        self.look = self.lexer.scan()
        return self

    def grammar(self):
        seq = []

        while True:
            rule = self.rule()
            if rule is None:
                break
            seq.append(rule)

        return seq

    def rule(self):
        if self.look is None:
            return None

        rule = self.lhs()
        self.match(Parser.EQUALS)
        definition = self.rhs()
        self.match(Parser.SEMICOLON)

        return Rule(rule, definition)

    def lhs(self):
        if self.look.tag == Token.RULE:
            token = self.look
            self.moveNext()
            return token
        self.error("Unexpect {0}".format(self.look))

    def rhs(self):
        token = None
        bracket = None

        if self.look == Parser.SEMICOLON:
            return None

        if self.look.tag in [Token.RULE, Token.LITERAL]:
            token = self.look

        if self.look == Token('[', Token.SYMBOL):
            bracket = Token(']', Token.SYMBOL)
            self.moveNext()
            token = Optional(self.rhs())
        elif self.look == Token('{', Token.SYMBOL):
            bracket = Token('}', Token.SYMBOL)
            self.moveNext()
            token = Repetition(self.rhs())
        elif self.look == Token('(', Token.SYMBOL):
            bracket = Token(')', Token.SYMBOL)
            self.moveNext()
            token = Grouping(self.rhs())

        if bracket is not None:
            if self.look != bracket:
                return self.error("Unclosed parentheses")
        self.moveNext()

        if self.look == Token('|', Token.SYMBOL):
            self.moveNext()
            return Alternation(token, self.rhs())

        if self.look == Token(',', Token.SYMBOL):
            self.moveNext()
            return Concatenation(token, self.rhs())

        return token

    def match(self, token):
        if self.look == token:
            return self.moveNext()
        self.error("Unexpect {0}".format(self.look))
