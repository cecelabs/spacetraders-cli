from abc import abstractmethod, ABC

from space_ui.domain.entities.contract import Contract


class TradingService(ABC):

    @abstractmethod
    def list_contracts(self) -> list[Contract]:
        raise NotImplementedError
