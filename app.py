from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.selectreactor import install
import logging

from NPSLoginProtocol import NPSLoginProtocolFactory

install()
from twisted.internet import reactor


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Server started")
    endpoint = TCP4ServerEndpoint(reactor, 8226)
    endpoint.listen(NPSLoginProtocolFactory())
    reactor.run()


if __name__ == "__main__":
    main()
