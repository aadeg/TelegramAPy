class ForceReplay:
    def __init__(self, force_reply, selective=None):
        self.force_reply = force_reply
        self.selective = selective

    def encode(self):
        out = {'force_reply': self.force_reply}
        if self.selective:
            out['selective'] = self.selective

        return out
