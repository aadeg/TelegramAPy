import json


class ForceReplay:
    FIELD_FORCEREPLY = 'force_reply'
    FIELD_SELECTIVE = 'selective'

    def __init__(self, force_reply, selective=None):
        self.force_reply = force_reply
        self.selective = selective

    def encode(self):
        out = {ForceReplay.FIELD_FORCEREPLY: self.force_reply}
        if self.selective:
            out[ForceReplay.FIELD_SELECTIVE] = self.selective

        return json.dumps(out)
