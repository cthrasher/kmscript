import dataclasses
import kingdom

@dataclasses.dataclass
class AssignLeadershipRoles:
		assignments: list[kingdom.Character]

@dataclasses.dataclass
class AdjustUnrest:
		event: int	

@dataclasses.dataclass
class ResourceCollection:
		bonus: int
		penalty: int

@dataclasses.dataclass
class PayConsumption:
		pass

@dataclasses.dataclass
class Upkeep:
		steps: tuple[AssignLeadershipRoles, AdjustUnrest, ResourceCollection, PayConsumption]
