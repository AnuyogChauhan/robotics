import json
import sys
from ens import ensclient


class RobotClientENS():
    def __init__(self):
        self.identifier = "markmiller.robotics02"
        self.network = "micro-robot-network.ping"
        self.my_ens_client = None

    def getValues(self, xVal, yVal, inverted ):
        self.my_ens_client = ensclient.ENSClient(self.identifier)
        if self.my_ens_client.init():
            s = self.my_ens_client.connect(self.network)
            if s:
                toRequest = dict()
                toRequest['x'] = xVal
                toRequest['y'] = yVal
                toRequest['inverted'] = inverted
                response = s.request(json.dumps(toRequest))
                print response
                return response
            else:
                print "failed to connect to ar-network"
                return None

        else:
            print "failed to initialize"
            sys.exit(1)

        return None

    def close(self):
        if self.my_ens_client is not None:
            self.my_ens_client.close()


if __name__ == "__main__":
    sc = RobotClientENS()
    sc.getValues(0.5, 0.5, False)
    sc.close()

