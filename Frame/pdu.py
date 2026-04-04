from abc import ABC, abstractmethod

class PDU(ABC):
    def __init__(self, payload: str):
        if type(self) is PDU:
            raise TypeError("PDU is abstract and cannot be instantiated directly")
        self._payload = payload

    def get_payload(self):
        return self._payload

    def set_payload(self, val: str):
        self._payload = val

    @abstractmethod
    def is_valid(self) -> bool:
        pass
