from pydantic.dataclasses import dataclass

@dataclass
class SettlementStatistics:
    level: int = 0
    blocks: int = 0
    lots: int = 0
    residential_lots: int = 0
    overcrowded: bool = False
    consumption: int = 0
    maximum_item_bonus: int = 0
    influence: int = 0
    
@dataclass
class ItemLevels:
    base: int = 0
    alchemical: int = 0
    arcane: int = 0
    divine: int = 0
    primal: int = 0
    luxurious: int = 0

@dataclass
class Agriculture:
    establish_farmland: int = 0
    harvest_crops: int = 0
    
@dataclass
class Arts:
	craft_luxuries: int = 0
	create_masterpiece: int = 0
	repair_reputation: int = 0
	rest_and_relax: int = 0
    
@dataclass
class Boating:
	go_fishing: int = 0
	rest_and_relax: int = 0

@dataclass
class Defense:
	fortify_hex: int = 0
	provide_care: int = 0

@dataclass
class Engineering:
	build_roads: int = 0
	demolish: int = 0
	establish_work_site: int = 0
	establish_work_site_lumber_camp: int = 0
	establish_work_site_mine: int = 0
	establish_work_site_quarry: int = 0
	irrigation: int = 0
	repair_reputation: int = 0

@dataclass
class Exploration:
	hire_adventurers: int = 0

@dataclass
class Folklore:
	celebrate_holiday: int = 0
	quell_unrest: int = 0

@dataclass
class Industry:
	relocate_capital: int = 0
	repair_reputation: int = 0
	trade_commodities: int = 0


@dataclass
class Intrigue:
	clandestine_business: int = 0
	infiltration: int = 0
	quell_unrest: int = 0

@dataclass
class Magic:
	prognostication: int = 0
	quell_unrest: int = 0
	supernatural_solution: int = 0

@dataclass
class Politics:
	improve_lifestyle: int = 0
	quell_unrest: int = 0

@dataclass
class Scholarship:
	creative_solution: int = 0
	rest_and_relax: int = 0

@dataclass
class Statecraft:
	request_foreign_aid: int = 0
	send_diplomatic_envoy: int = 0
	tap_treasury: int = 0

@dataclass
class Trade:
	capital_investment: int = 0
	collect_taxes: int = 0
	manage_trade_agreements: int = 0
	purchase_commodities: int = 0
	repair_reputation: int = 0
	rest_and_relax: int = 0

@dataclass
class Warfare:
	pledge_of_fealty: int = 0
	quell_unrest: int = 0

@dataclass
class Wilderness:
	gather_livestock: int = 0
	rest_and_relax: int = 0

@dataclass
class Any:
	focused_attention: int = 0

@dataclass
class General:
	abandon_hex: int = 0
	build_structure: int = 0
	claim_hex: int = 0
	clear_hex: int = 0
	establish_settlement: int = 0
	establish_trade_agreement: int = 0
	new_leadership: int = 0
	pledge_of_fealty: int = 0
	quell_unrest: int = 0
	repair_reputation: int = 0
	rest_and_relax: int = 0

@dataclass
class Army:
	recover_army: int = 0
	recruit_army: int = 0
	train_army: int = 0
		
@dataclass
class Settlement:
	stats: SettlementStatistics
	item_levels: ItemLevels
	agriculture: Agriculture
	arts: Arts
	boating: Boating
	defense: Defense
	engineering: Engineering
	exploration: Exploration
	folklore: Folklore
	industry: Industry
	intrigue: Intrigue
	magic: Magic
	politics: Politics
	scholarship: Scholarship
	statecraft: Statecraft
	trade: Trade
	warfare: Warfare
	wilderness: Wilderness
	any: Any
	general: General
	army: Army
