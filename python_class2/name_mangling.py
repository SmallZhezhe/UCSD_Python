"""Example of name mangling; enter in the REPL"""
class Test:
    def __mangled_name(self):
        pass
    def normal_name(self):
        pass
    def _protected_name(self):
        pass

t = Test()

[attr for attr in dir(t) if 'name' in attr]
