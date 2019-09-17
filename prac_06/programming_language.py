class ProgrammingLanguage:

    def __init__(self, name="", dynamic="", is_reflection=False, year=0):
        self.name = name
        self.dynamic = dynamic
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        if self.is_dynamic == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.dynamic, self.is_reflection,
                                                                          self.year)
