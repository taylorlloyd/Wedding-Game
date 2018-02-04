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

class GroomSchoolRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.groom_school_friend == True
    def rule_text(self):
        return groom+"'s school friends"

class BrideSchoolRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.bride_school_friend == True
    def rule_text(self):
        return bride+"'s school friends"

class GroomTechRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.groom_tech_friend == True
    def rule_text(self):
        return groom+"'s tech friends"

class BrideMedRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.bride_medical_friend == True
    def rule_text(self):
        return bride+"'s medical friends"

class ParentRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.parent == True
    def rule_text(self):
        return "any parents"

class NonParentRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.parent == False
    def rule_text(self):
        return "anyone who isn't a parent"

class FamilyFriendRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.family_friend == True
    def rule_text(self):
        return "any family friends (bride or groom)"

class LocalRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.from_alberta == True
    def rule_text(self):
        return "anyone living in Alberta"

class RemoteRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.from_alberta == False
    def rule_text(self):
        return "anyone living outside Alberta"

class JustMetRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.just_met == True
    def rule_text(self):
        return "anyone who met the bride or groom here"

class SingleRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.came_alone == True
    def rule_text(self):
        return "anyone who came single to the wedding"

class CoupleRule(Rule):
    def __init__(self):
        pass
    def matches(self, source, target):
        return target.came_alone == False
    def rule_text(self):
        return "anyone who came to the wedding with a +1"

Rules = [
    GroomRelativeRule(),
    BrideRelativeRule(),
    GroomSchoolRule(),
    BrideSchoolRule(),
    GroomTechRule(),
    BrideMedRule(),
    ParentRule(),
    NonParentRule(),
    FamilyFriendRule(),
    LocalRule(),
    RemoteRule(),
    JustMetRule(),
    SingleRule(),
    CoupleRule(),
]
