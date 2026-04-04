from eth_frame import EthFrame

frame = EthFrame(
    dmac="AA:BB:CC:DD:EE:FF",
    smac="11:22:33:44:55:66",
    eth_type=0x0800,
    payload="Hello World"
)

print(frame)
print("Valid:", frame.is_valid())

# změna payloadu → přepočet FCS
frame.set_payload("New Data")
print("Valid after change:", frame.is_valid())

# simulace chyby
frame.corrupt_data()
print("Valid after corruption:", frame.is_valid())
