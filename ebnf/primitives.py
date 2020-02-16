# -*- coding:utf-8 -*-


class Stmt:
    def asString(self):
        raise Exception("Missing `asString` method")

    def __repr__(self):
        return self.asString()

    def __str__(self):
        return self.asString()


class Optional(Stmt):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def asString(self):
        return "Optional({0})".format(self.token.asString())


class Repetition(Stmt):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def asString(self):
        return "Repetition({0})".format(self.token.asString())


class Grouping(Stmt):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def asString(self):
        return "Grouping({0})".format(self.token.asString())


class Alternation(Stmt):
    def __init__(self, token, tail):
        super().__init__()
        self.token = token
        self.tail = tail

    def asString(self):
        return "Alternation({0}, {1})".format(
            self.token.asString(), self.tail.asString()
        )


class Concatenation(Stmt):
    def __init__(self, token, tail):
        super().__init__()
        self.token = token
        self.tail = tail

    def asString(self):
        return "Concatenation({0}, {1})".format(
            self.token.asString(), self.tail.asString()
        )


class Rule(Stmt):
    def __init__(self, rule, stmt, *args, **kwargs):
        self.rule = rule
        self.stmt = stmt

    def asString(self):
        return "Rule({0} = {1})".format(
            self.rule.asString(), self.stmt.asString()
        )
