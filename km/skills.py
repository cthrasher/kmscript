from enum import Enum, auto

from .keyabilities import *

class Agriculture:
    @staticmethod
    def key_ability(): return Stability
    
class Arts:
    @staticmethod
    def key_ability(): return Culture
    
class Boating:
    @staticmethod
    def key_ability(): return Economy

class Defense:
    @staticmethod
    def key_ability(): return Stability

class Engineering:
    @staticmethod
    def key_ability(): return Stability

class Exploration:
    @staticmethod
    def key_ability(): return Economy

class Folklore:
    @staticmethod
    def key_ability(): return Culture

class Industry:
    @staticmethod
    def key_ability(): return Economy

class Intrigue:
    @staticmethod
    def key_ability(): return Loyalty

class Magic:
    @staticmethod
    def key_ability(): return Culture

class Politics:
    @staticmethod
    def key_ability(): return Loyalty

class Scholarship:
    @staticmethod
    def key_ability(): return Culture

class Statecraft:
    @staticmethod
    def key_ability(): return Loyalty

class Trade:
    @staticmethod
    def key_ability(): return Economy

class Warfare:
    @staticmethod
    def key_ability(): return Loyalty

class Wilderness:
    @staticmethod
    def key_ability(): return Stability
