# -*- coding:utf-8 -*-

import unittest
from ebnf.exception import SyntaxException
from ebnf.lexer import Lexer, Token


class TestLexerCase(unittest.TestCase):
    def test_doubleQuote(self):
        self.assertEqual(
            Lexer('letter = "A" ;').scanAll(), [
                Token("letter", Token.RULE),
                Token('=', Token.SYMBOL),
                Token('A', Token.LITERAL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_singleQuote(self):
        self.assertEqual(
            Lexer("letter = 'A';").scanAll(), [
                Token("letter", Token.RULE),
                Token('=', Token.SYMBOL),
                Token('A', Token.LITERAL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_id(self):
        self.assertEqual(
            Lexer("A = B ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('B', Token.RULE),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_idOrId(self):
        self.assertEqual(
            Lexer("A = B | C ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('B', Token.RULE),
                Token('|', Token.SYMBOL),
                Token('C', Token.RULE),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_idAndId(self):
        self.assertEqual(
            Lexer("A = B, C ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('B', Token.RULE),
                Token(',', Token.SYMBOL),
                Token('C', Token.RULE),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_brackets(self):
        self.assertEqual(
            Lexer("A = ( B ) ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('(', Token.SYMBOL),
                Token('B', Token.RULE),
                Token(')', Token.SYMBOL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_curlyBrackets(self):
        self.assertEqual(
            Lexer("A = { B } ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('{', Token.SYMBOL),
                Token('B', Token.RULE),
                Token('}', Token.SYMBOL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_squareBrackets(self):
        self.assertEqual(
            Lexer("A = [ B ] ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('[', Token.SYMBOL),
                Token('B', Token.RULE),
                Token(']', Token.SYMBOL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_multiline(self):
        self.assertEqual(
            Lexer('A = ( B );\nB = "C" ;').scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('(', Token.SYMBOL),
                Token('B', Token.RULE),
                Token(')', Token.SYMBOL),
                Token(';', Token.SYMBOL),
                Token('B', Token.RULE),
                Token('=', Token.SYMBOL),
                Token('C', Token.LITERAL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_invalidRule1(self):
        with self.assertRaises(SyntaxException):
            Lexer('A = "C').scanAll()

    def test_invalidRule2(self):
        with self.assertRaises(SyntaxException):
            Lexer("A = 'C").scanAll()

    def test_whitespace(self):
        self.assertEqual(
            Lexer("A = ' ' | '\\t' | '\\r' | '\\n' ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token(' ', Token.LITERAL),
                Token('|', Token.SYMBOL),
                Token('\t', Token.LITERAL),
                Token('|', Token.SYMBOL),
                Token('\r', Token.LITERAL),
                Token('|', Token.SYMBOL),
                Token('\n', Token.LITERAL),
                Token(';', Token.SYMBOL)
            ]
        )

    def test_backslash(self):
        self.assertEqual(
            Lexer("A = '\\'' | \"\\\"\" ;").scanAll(), [
                Token('A', Token.RULE),
                Token('=', Token.SYMBOL),
                Token("'", Token.LITERAL),
                Token('|', Token.SYMBOL),
                Token('"', Token.LITERAL),
                Token(';', Token.SYMBOL)
            ]
        )
