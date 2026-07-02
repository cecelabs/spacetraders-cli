from space_ui.domain.entities.contract import Contract
from space_ui.domain.interfaces import TradingService
from src.traders.infraestructure.services.space_traders_service import SpaceTradersService
from src.traders.domain.entities.contract import Contract as STContract
space_traders=SpaceTradersService()

class CustomTraderService(TradingService):

    def list_contracts(self) -> list[Contract]:
        contracts_data = [
            {
                "id": "#TRAD-447",
                "type": "PROCUREMENT",
                "status": "Active",
                "faction_symbol": "Cosmic Syndicate",
                "order": "Deliver 20 units of refined Fuel to Andromeda Station to resupply long-haul freighters.",

                "fuel": "20x Fuel",
                "location": "X1-ANDROMEDA-7",
                "credits": "47,000 CR",
                "status_order": "Delivery Progress",
                "status_order_num": 50,
                "items": "10 / 20",

                "on_accept": "On Accept: +5,000 CR",
                "on_fulfill": "On Fulfill: +42,000 CR",
                "expiration": "16h 0m remaining"
            },
        ]
        list_st_contracts: list[STContract]=space_traders.get_contracts()
        list_contracts: list[Contract]=[]
        for stcontract in list_st_contracts:
            contract=Contract(
                id=f"ID: {stcontract.id[:4]}",
                type=stcontract.type,
                status="Active" if stcontract.accepted else "Inactive",
                location=stcontract.faction_symbol,
                expiration=stcontract.expiration,
                faction_symbol=stcontract.faction_symbol,
                fuel="fuel revisa backend"
            )
            list_contracts.append(contract)
        #return Contract.from_list(contracts_data)
        return list_contracts


if __name__ == "__main__":
    data = CustomTraderService().list_contracts()
    print(data)
