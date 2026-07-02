from pydantic import BaseModel


class Contract(BaseModel):
    id: str
    type: str
    status: str
    location: str
    expiration: str
    faction_symbol: str
    fuel: str
    on_accept: str | None = None
    on_fulfill: str | None = None
    credits: str | None = None
    status_order: str | None = None
    status_order_num: int | None = None
    items: str | None = None
    order: str | None = None

    @classmethod
    def from_list(cls, contracts_list: list[dict]) -> list["Contract"]:
        contracts = []
        for contract_dict in contracts_list:
            contracts.append(
                cls(**contract_dict)
            )
        return contracts
