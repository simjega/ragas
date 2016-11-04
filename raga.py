# Central definition of what a raga is
# Rules that apply so far:
# Must be 5-7 notes from the given 12 possible notes
# Must have an upwards and downwards movement
# This entire framework is a relative scale


class Raga(object):
    def __init__(self, aroha, avroha):
        self.aroha = aroha
        self.avroha = avroha

    def __repr__(self):
        return "^ " + self.aroha.__repr__() + "\n" + "v " + self.avroha.__repr__() + "\n"
