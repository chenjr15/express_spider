

class StopNode:
    '''Model for every node of express stop.'''

    def __init__(self, name, timestamp, status, next_stop=None):
        self.name = name
        self.timestamp = timestamp
        self.status = status
        self.next_stop = next_stop

    def __format__(self,fmt):
        fmtstr = self.name
        if (self.status.find("发出") is not -1):
            fmtstr += "-->"
        return fmtstr
