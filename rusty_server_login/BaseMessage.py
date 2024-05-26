from .util import MessageVersion, bigEndianBytesToInt


class BaseMessage:
    def __init__(self, msg_version: MessageVersion, data: bytes):
        self.msg_version = msg_version
        self.msgId = bigEndianBytesToInt(data[0:2])
        self.msgLen = bigEndianBytesToInt(data[2:4])
                
        if msg_version == MessageVersion.V1:
            if len(data) < 12:
                raise ValueError(
                    "Message is too short, expected at least 12 bytes, got "
                    + str(len(data))
                    + " bytes."
                )
            self.data = data[12:]
        else:
            if len(data) < 6:
                raise ValueError(
                    "Message is too short, expected at least 6 bytes, got "
                    + str(len(data))
                    + " bytes."
                )
            self.data = data[6:]

    def to_json(self):
        return {
            'msg_version': self.msg_version.name,
            'msg_id': self.msgId,
            'msg_len': self.msgLen,
            'data': self.data.hex(' ', 0)
        }

    def __str__(self):
        return str(self.to_json())
