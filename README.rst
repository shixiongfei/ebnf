ebnf
====

An EBNF parser

Example
-------

Wikipedia EBNF Examples
~~~~~~~~~~~~~~~~~~

https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form

.. code-block:: python

    source = """
    letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
        | "H" | "I" | "J" | "K" | "L" | "M" | "N"
        | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
        | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
        | "c" | "d" | "e" | "f" | "g" | "h" | "i"
        | "j" | "k" | "l" | "m" | "n" | "o" | "p"
        | "q" | "r" | "s" | "t" | "u" | "v" | "w"
        | "x" | "y" | "z" ;
    digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
    symbol = "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
        | "'" | '"' | "=" | "|" | "." | "," | ";" ;
    character = letter | digit | symbol | "_" ;
    
    identifier = letter , { letter | digit | "_" } ;
    terminal = "'" , character , { character } , "'" 
            | '"' , character , { character } , '"' ;
    
    lhs = identifier ;
    rhs = identifier
        | terminal
        | "[" , rhs , "]"
        | "{" , rhs , "}"
        | "(" , rhs , ")"
        | rhs , "|" , rhs
        | rhs , "," , rhs ;

    rule = lhs , "=" , rhs , ";" ;
    grammar = { rule } ;
    """

Lexer Example
~~~~~~~~~~~~~

.. code-block:: python

    from ebnf.lexer import Lexer

    lexer = Lexer(source)
    
    while True:
        token = lexer.scan()
        if token is None:
            break
        print(token)

Parser Example
~~~~~~~~~~~~~

.. code-block:: python

    from ebnf.lexer import Lexer
    from ebnf.parser import Parser

    parser = Parser(Lexer(source))
    program = parser.grammar()
    for rule in program:
        print(rule)
