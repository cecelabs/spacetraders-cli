import reflex as rx

from space_ui.domain.entities.contract import Contract
from space_ui.infraestructure.services.custom_trader import CustomTraderService


class ContractState(rx.State):
    contract: Contract = Contract(
        id="",
        type="",
        status="",
        location="",
        expiration="",
        faction_symbol="",
        fuel=""
    )

    def set_contract(self, contract: Contract):
        self.contract = contract


class ContractsState(rx.State):
    contracts: list[Contract] = [Contract(
        id="",
        type="",
        status="",
        location="",
        expiration="",
        faction_symbol="",
        fuel=""
    )]

    def load_contracts(self):
        self.contracts = CustomTraderService().list_contracts()
