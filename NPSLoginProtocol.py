from twisted.internet.protocol import Protocol, Factory
import logging
from rusty_server_login.util import getMessageVersion
from rusty_server_login.BaseMessage import BaseMessage


class NPSLoginProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.logger = logging.getLogger("NPSLoginProtocol")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())

    def connectionMade(self):
        self.logger.info("Connection from: %s", self.transport.getPeer())

    def dataReceived(self, data):
        version = getMessageVersion(data)
        self.logger.info("Message version: %s", version)
        message = BaseMessage(version, data)
        self.logger.info("Data received: %s", data.hex(" ", 0))
        self.logger.info("Message: %s", message)
        self.transport.write(data)

    def connectionLost(self, reason):
        self.logger.info("Connection lost: %s", reason)


class NPSLoginProtocolFactory(Factory):
    protocol = NPSLoginProtocol

    def __init__(self):
        self.logger = logging.getLogger("NPSLoginProtocol")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.info("Factory created")

    def buildProtocol(self, addr):
        return NPSLoginProtocol(self)
