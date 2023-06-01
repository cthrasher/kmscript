class Phase():
    def __init__(self, step = 0):
        self._step = step

    def current(self):
        return (self.__class__.__name__, self.STEPS[self._step])

    def next(self):
        if self._step + 1 == len(self.STEPS):
            return self.NEXT(step = 0)
        else:
            return self.__class__(step = self._step + 1)

# Interphase is anything outside of the kingdom turn
class Interphase(Phase):
    STEPS = ["Interphase"]
    NEXT = None

class Upkeep(Phase):
    STEPS = [
        "Assign Leadership Roles",
        "Adjust Unrest",
        "Resource Collection",
        "Pay Consumption",
    ]
    NEXT = None

class Commerce(Phase):
    STEPS = [
        "Collect Taxes",
        "Approve Expenses",
        "Tap Commodities",
        "Manage Trade Agreements",
		]
    NEXT = None

class Activity(Phase):
    STEPS = [
        "Leadership Activities",
        "Region Activities",
        "Civic Activities",
		]
    NEXT = None

class Event(Phase):
    STEPS = [
        "Check for a Random Event",
        "Event Resolution",
        "Apply Kingdom XP",
        "Increase Kingdom Level",
    ]
    NEXT = None

# If we try to set this in the class definition, there is a referential loop.
Interphase.NEXT = Upkeep
Upkeep.NEXT = Commerce
Commerce.NEXT = Activity
Activity.NEXT = Event
Event.NEXT = Interphase

__all__ = [
        "Interphase",
        "Upkeep",
        "Commerce",
        "Activity",
        "Event",
    ]
