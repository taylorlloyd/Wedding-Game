from random import random
groom="Taylor"
bride="Maddy"

class Rule:
    def __init__(self):
        pass

    def matches(self, source, target):
        return False

    def rule_text(self):
        return "Generic Rule Superclass"

class GroomRelativeRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.groom_relative == True
    def rule_text(self):
        return groom+"'s relatives"

class BrideRelativeRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.bride_relative == True
    def rule_text(self):
        return bride+"'s relatives"

Rules = [
    GroomRelativeRule(),
    BrideRelativeRule(),
]
