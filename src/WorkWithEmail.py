import abc
import time


class OtherProgramInteraction(abc.ABC):
    @abc.abstractmethod
    def sendInEmail(self, result):
        pass

class WorkWithEmail(OtherProgramInteraction):
    def sendInEmail(self, result):
        time.sleep(2)
