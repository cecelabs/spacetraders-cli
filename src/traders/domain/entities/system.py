from dataclasses import dataclass

from reflex_components_radix.themes.components.data_list import data_list


@dataclass
class System():
    constellation: str
    symbol: str
    sector_symbol: str
    type: str
    x: int
    y: int

    @classmethod
    def from_dict(cls, data: dict)->"System":
        return cls(
            constellation=data["constellation"],
            symbol=data["symbol"],
            sector_symbol=data["sectorSymbol"],
            type=data["type"],
            x=data["x"],
            y=data["y"],
        )

    @classmethod
    def from_list(cls, data_list: list[dict])->list["System"]:
        systems=[]
        for system_dict in data_list:
            systems.append(cls.from_dict(system_dict))
        return systems



