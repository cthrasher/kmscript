import dataclasses
import enum

class Role(enum.Enum):
	RULER = 0
	COUNSELOR = 1
	GENERAL = 2
	EMISSARY = 3
	MAGISTER = 4
	TREASURER = 5
	VICEROY = 6
	WARDEN = 7

class Skill(enum.Enum):
	AGRICULTURE = enum.auto()
	ARTS = enum.auto()
	BOATING = enum.auto()
	DEFENSE = enum.auto()
	ENGINEERING = enum.auto()
	EXPLORATION = enum.auto()
	FOLKLORE = enum.auto()
	INDUSTRY = enum.auto()
	INTRIGUE = enum.auto()
	MAGIC = enum.auto()
	POLITICS = enum.auto()
	SCHOLARSHIP = enum.auto()
	STATECRAFT = enum.auto()
	TRADE = enum.auto()
	WARFARE = enum.auto()
	WILDERNESS = enum.auto()

@dataclasses.dataclass
class Statistics:
		generic: int
		culture: int
		economy: int
		loyalty: int
		stability: int
		fame: int
		corruption: int
		crime: int
		unrest: int
		decay: int
		strife: int
		rp: int
		food: int
		lumber: int
		luxuries: int
		ore: int
		stone: int
		control_dc: int


@dataclasses.dataclass
class Character:
		name: str
		npc: bool
		role: Role

@dataclasses.dataclass
class Proficiency:
		skill: Skill
		modifier: int

@dataclasses.dataclass
class Kingdom:
		_statistics: Statistics
		_proficiencies: dict[Skill, int]
		_characters: list[Character]
