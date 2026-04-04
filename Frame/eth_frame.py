import re
from pdu import PDU


class EthFrame(PDU):

    def __init__(self, dmac: str, smac: str, eth_type: int, payload: str, fcs=None):
        super().__init__(payload)

        if not self.is_valid_mac(dmac) or not self.is_valid_mac(smac):
            raise ValueError("Invalid MAC address format")

        self._dmac = dmac
        self._smac = smac
        self._type = eth_type

        if fcs is None:
            self._fcs = self.calculate_fcs()
        else:
            self._fcs = fcs

    @staticmethod
    def is_valid_mac(mac: str) -> bool:
        pattern = r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"
        return re.match(pattern, mac) is not None

    def get_dmac(self):
        return self._dmac

    def set_dmac(self, val):
        if not self.is_valid_mac(val):
            raise ValueError("Invalid MAC")
        self._dmac = val
        self._recalculate_fcs()

    def get_smac(self):
        return self._smac

    def set_smac(self, val):
        if not self.is_valid_mac(val):
            raise ValueError("Invalid MAC")
        self._smac = val
        self._recalculate_fcs()

    def get_type(self):
        return self._type

    def set_type(self, val):
        self._type = val
        self._recalculate_fcs()

    def set_payload(self, val):
        super().set_payload(val)
        self._recalculate_fcs()

    def get_fcs(self):
        return self._fcs

    def calculate_fcs(self) -> int:
        data = f"{self._dmac}{self._smac}{self._type}{self._payload}"
        return sum(ord(c) for c in data)

    def _recalculate_fcs(self):
        self._fcs = self.calculate_fcs()

    def is_valid(self) -> bool:
        return self.calculate_fcs() == self._fcs

    def __str__(self):
        return f"[EthFrame] SRC: {self._smac} DST: {self._dmac} TYPE: {hex(self._type)} DATA: {self._payload}"


    def corrupt_data(self):
        self._payload = "!!!CORRUPTED!!!"
        self._fcs = 123456 
