# -*- coding:utf-8 -*-

import unittest
from ebnf.lexer import Lexer, Token
from ebnf.parser import Parser


class TestParserCase(unittest.TestCase):
    def test_Parse(self):
        ast = Parser(Lexer('letter = "A" ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('letter', Token.RULE))
        self.assertEqual(ast[0].stmt, Token('A', Token.LITERAL))

    def test_id(self):
        ast = Parser(Lexer('A = B ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt, Token('B', Token.RULE))

    def test_idOrId(self):
        ast = Parser(Lexer('A = B | C ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt.__class__.__name__, "Alternation")
        self.assertEqual(ast[0].stmt.lhs, Token('B', Token.RULE))
        self.assertEqual(ast[0].stmt.rhs, Token('C', Token.RULE))

    def test_idAndId(self):
        ast = Parser(Lexer('A = B , C ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt.__class__.__name__, "Concatenation")
        self.assertEqual(ast[0].stmt.lhs, Token('B', Token.RULE))
        self.assertEqual(ast[0].stmt.rhs, Token('C', Token.RULE))

    def test_brackets(self):
        ast = Parser(Lexer('A = ( B ) ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt.__class__.__name__, "Grouping")
        self.assertEqual(ast[0].stmt.token, Token('B', Token.RULE))

    def test_curlyBrackets(self):
        ast = Parser(Lexer('A = { B } ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt.__class__.__name__, "Repetition")
        self.assertEqual(ast[0].stmt.token, Token('B', Token.RULE))

    def test_squareBrackets(self):
        ast = Parser(Lexer('A = [ B ] ;')).grammar()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt.__class__.__name__, "Optional")
        self.assertEqual(ast[0].stmt.token, Token('B', Token.RULE))

    def test_multiline(self):
        ast = Parser(Lexer('A = ( B );\nB = "C" ;')).grammar()

        self.assertEqual(len(ast), 2)

        self.assertEqual(ast[0].rule, Token('A', Token.RULE))
        self.assertEqual(ast[0].stmt.__class__.__name__, "Grouping")
        self.assertEqual(ast[0].stmt.token, Token('B', Token.RULE))

        self.assertEqual(ast[1].rule, Token('B', Token.RULE))
        self.assertEqual(ast[1].stmt, Token('C', Token.LITERAL))
