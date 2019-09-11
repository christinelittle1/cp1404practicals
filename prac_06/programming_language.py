class ProgrammingLanguage:

    def __init__(self, name="", is_dynamic=False, is_reflection=False, year=0):
        self.name = name
        self.is_dynamic = is_dynamic
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        if self.is_dynamic == "Dynamic":
            return True
        else:
            return False
