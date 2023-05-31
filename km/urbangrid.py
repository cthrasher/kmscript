from pydantic.dataclasses import dataclass
from enum import Enum, auto

class CardinalDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

@dataclass
class LotGroup:
    lots: tuple[Building, Building, Building, Building]

@dataclass
class Border:
    water: bool = False
    bridge: bool = False
    wall_wooden: bool = False
    wall_stone: bool = False

@dataclass
class UrbanGrid:
    borders: tuple[Border, Border, Border, Border]
    lots: tuple[
        tuple[LotGroup, LotGroup, LotGroup],
        tuple[LotGroup, LotGroup, LotGroup],
        tuple[LotGroup, LotGroup, LotGroup],
    ]
