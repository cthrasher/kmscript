# Q: Why is this code and not data?
# A: Eventually there will be code attached to each of these things for check consequences, etc.

class AbandonHex:
    NAME = "Abandon Hex"
    TAGS = ["downtime", "region"]
    SKILLS = ["Exploration", "Wilderness"]
    STEPS = [("Activity", "Region Activities")]
    TRAINED = False

class BuildStructure:
    NAME = "Build Structure"
    TAGS = ["civic", "downtime"]
    SKILLS = ["Any"] # Parameterized by structure
    STEPS = [("Activity", "Civic Activities")]
    TRAINED = False

class ClaimHex:
    NAME = "Claim Hex"
    TAGS = ["downtime", "region"]
    SKILLS = ["Exploration", "Intrigue", "Magic", "Wilderness"]
    STEPS = [("Activity", "Region Activities")]
    TRAINED = False

class ClearHex:
    NAME = "Clear Hex"
    TAGS = ["downtime", "region"]
    SKILLS = ["Engineering", "Exploration"] # Skill and DC determined by nature of clear
    STEPS = [("Activity", "Region Activities")]
    TRAINED = False

class EstablishSettlement:
    NAME = "Establish Settlement"
    TAGS = ["downtime", "region"]
    SKILLS = ["Engineering", "Industry", "Politics", "Scholarship"]
    STEPS = [("Activity", "Region Activities")]
    TRAINED = False

class EstablishTradeAgreement:
    NAME = "Establish Trade Agreement"
    TAGS = ["downtime", "leadership"]
    SKILLS = ["Boating", "Magic", "Trade"] # Skill determined situationally
    STEPS = [("Activity", "Leadership Activities")]
    TRAINED = False

class FocusedAttention:
    NAME = "Focused Attention"
    TAGS = ["downtime", "leadership"]
    SKILLS = ["Any"]
    STEPS = [("Activity", "Leadership Activities")]
    TRAINED = False

class NewLeadership:
    NAME = "New Leadership"
    TAGS = ["downtime"]
    SKILLS = ["Intrigue", "Politics", "Statecraft", "Warfare"]
    STEPS = [("Any", "Any")]
    TRAINED = False

class PledgeOfFealty:
    NAME = "Pledge of Fealty"
    TAGS = ["downtime", "leadership"]
    SKILLS = ["Intrigue", "Statecraft", "Warfare"]
    STEPS = [("Activity", "Leadership Activities")]
    TRAINED = True

# Quell Unrest
# Repair Reputation
# Rest and Relax
# Establish Farmland
# Harvest Crops
# Craft Luxuries
# Create a Masterpiece
# Go Fishing
# Fortify Hex
# Provide Care
# Build Roads
# Establish Worksite
# Irrigation
# Hire Adventurers
# Celebrate Holiday

class TradeCommodities:
    NAME = "Trade Commodities"
    TAGS = ["commerce", "downtime"]
    SKILLS = ["Industry"]
    STEPS = [("Commerce", "Tap Commodities")]
    TRAINED = False

# Relocate Capital
# Infiltration
# Clandestine Business
# Supernatural Solution
# Prognostication
# Improve Lifestyle
# Creative Solution
# Tap Treasury
# Request Foreign Aid
# Send Diplomatic Envoy
# Capital Investment
# Manage Trade Agreements
# Purchase Commodities
# Collect Taxes
# Gather Livestock

class Activities:
    # TODO: Use reflection to derive this instead
    ACTIVITIES = [
        AbandonHex,
        BuildStructure,
        ClaimHex,
        ClearHex,
        EstablishSettlement,
        EstablishTradeAgreement,
        FocusedAttention,
        NewLeadership,
        PledgeOfFealty,
        TradeCommodities,
    ]

    @classmethod
    def available(cls, step):
        for activity in cls.ACTIVITIES:
            if step in activity.STEPS or ("Any", "Any") in activity.STEPS:
                yield activity
