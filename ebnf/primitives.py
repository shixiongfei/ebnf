# -*- coding:utf-8 -*-


class Statement:
    def asString(self):
        raise Exception("Missing `asString` method")

    def __repr__(self):
        return self.asString()

    def __str__(self):
        return self.asString()


class Optional(Statement):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def asString(self):
        return "Optional({0})".format(self.token.asString())


class Repetition(Statement):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def asString(self):
        return "Repetition({0})".format(self.token.asString())


class Grouping(Statement):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def asString(self):
        return "Grouping({0})".format(self.token.asString())


class Alternation(Statement):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.lhs = lhs
        self.rhs = rhs

    def asString(self):
        return "Alternation({0}, {1})".format(
            self.lhs.asString(), self.rhs.asString()
        )


class Concatenation(Statement):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.lhs = lhs
        self.rhs = rhs

    def asString(self):
        return "Concatenation({0}, {1})".format(
            self.lhs.asString(), self.rhs.asString()
        )


class Rule(Statement):
    def __init__(self, rule, stmt, *args, **kwargs):
        self.rule = rule
        self.stmt = stmt

    def asString(self):
        return "Rule({0} = {1})".format(
            self.rule.asString(), self.stmt.asString()
        )
