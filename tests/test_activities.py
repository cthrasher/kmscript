import km
import pytest

@pytest.fixture
def truth():
    return {
        ('Interphase', 'Interphase'): [
            "New Leadership",
        ],
        ('Upkeep', 'Assign Leadership Roles'): [
            "New Leadership",
        ],
        ('Upkeep', 'Adjust Unrest'): [
            "New Leadership",
        ],
        ('Upkeep', 'Resource Collection'): [
            "New Leadership",
        ],
        ('Upkeep', 'Pay Consumption'): [
            "New Leadership",
        ],
        ('Commerce', 'Collect Taxes'): [
            "New Leadership",
        ],
        ('Commerce', 'Approve Expenses'): [
            "New Leadership",
        ],
        ('Commerce', 'Tap Commodities'): [
            "New Leadership",
            "Trade Commodities",
        ],
        ('Commerce', 'Manage Trade Agreements'): [
            "New Leadership",
        ],
        ('Activity', 'Leadership Activities'): [
            "Establish Trade Agreement",
            "Focused Attention",
            "New Leadership",
            "Pledge of Fealty",
        ],
        ('Activity', 'Region Activities'): [
            "Abandon Hex",
            "Claim Hex",
            "Clear Hex",
            "Establish Settlement",
            "New Leadership",
        ],
        ('Activity', 'Civic Activities'): [
            "Build Structure",
            "New Leadership",
        ],
        ('Event', 'Check for a Random Event'): [
            "New Leadership",
        ],
        ('Event', 'Event Resolution'): [
            "New Leadership",
        ],
        ('Event', 'Apply Kingdom XP'): [
            "New Leadership",
        ],
        ('Event', 'Increase Kingdom Level'): [
            "New Leadership",
        ],
    }

def test_activities(truth):
    state = km.Interphase()
    states = set()
    while True:
        pair = state.current()
        if pair in states: break
        states.add(pair)
        for activity in km.Activities.available(pair):
            assert activity.NAME in truth[pair]
        state = state.next()

def test_monkeypatch(truth):
    class TakeCharge:
        NAME = "Take Charge"
        TAGS = ["leadership", "downtime"]
        SKILLS = ["Any"]
        STEPS = [("Activity", "Leadership Activities")]
        TRAINED = True
    km.Activities.ACTIVITIES.append(TakeCharge)
    pair = ("Activity", "Leadership Activities")
    for activity in km.Activities.available(pair):
        assert activity.NAME in truth[pair] or activity.NAME == "Take Charge"
