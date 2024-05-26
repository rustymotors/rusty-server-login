from enum import Enum


class MessageVersion(Enum):
    V0 = '1.0'
    V1 = '1.1'


def littleEndianBytesToInt(data: bytes) -> int:
    return int.from_bytes(data, byteorder="little")

def bigEndianBytesToInt(data: bytes) -> int:
    return int.from_bytes(data, byteorder="big")


def getMessageVersion(msg: bytes) -> str:

    if len(msg) < 6:
        raise ValueError(
            "Message is too short, expected at least 6 bytes, got "
            + str(len(msg))
            + " bytes."
        )

    # Get the message version
    version = littleEndianBytesToInt(msg[4:6])

    if version == 0x0101:
        return MessageVersion.V1
    if version == 0:
        return MessageVersion.V0

    raise ValueError("Unknown message version: " + str(version))
