import km

def test_phases():
    steps = (
        ("Interphase", "Interphase"),
        ("Upkeep", "Assign Leadership Roles"),
        ("Upkeep", "Adjust Unrest"),
        ("Upkeep", "Resource Collection"),
        ("Upkeep", "Pay Consumption"),
        ("Commerce", "Collect Taxes"),
        ("Commerce", "Approve Expenses"),
        ("Commerce", "Tap Commodities"),
        ("Commerce", "Manage Trade Agreements"),
        ("Activity", "Leadership Activities"),
        ("Activity", "Region Activities"),
        ("Activity", "Civic Activities"),
        ("Event", "Check for a Random Event"),
        ("Event", "Event Resolution"),
        ("Event", "Apply Kingdom XP"),
        ("Event", "Increase Kingdom Level"),
        ("Interphase", "Interphase"),
    )
    state = km.Interphase()
    for pair in steps:
        assert(pair == state.current())
        state = state.next()
