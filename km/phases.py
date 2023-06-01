class Phase():
    def __init__(self, step = 1):
        self._step = step

    def current(self):
        return (self.__name__, self.STEPS[self._step - 1])

    def next(self):
        if self._step + 1 == len(self.STEPS):
            return self.NEXT()
        else:
            return self._class__(self.step + 1)

class Interphase(Phase):
    STEPS = ["Interphase"]
    NEXT = Upkeep

class Upkeep(Phase):
    STEPS = [
        "Assign Leadership Roles",
        "Adjust Unrest",
        "Resource Collection",
        "Pay Consumption",
    ]
    NEXT = Commerce

class Commerce(Phase):
    STEPS = [
        "Collect Taxes",
        "Approve Expenses",
        "Tap Commodities",
        "Mange Trade Agreements",
		]
    NEXT = Activity

class Activity(Phase):
    STEPS = [
        "Leadership Activities",
        "Region Activities",
        "Civic Activities",
		]
    NEXT = Event

class Event(Phase):
    STEPS = [
        "Check for a Random Event",
        "Event Resolution",
        "Apply Kingdom XP",
        "Increase Kingdom Level",
    ]
    NEXT = Interphase

__all__ = [Interphase, Upkeep, Commerce, Activity, Event]
