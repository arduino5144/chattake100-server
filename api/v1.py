class Plugin:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(cls.__name__)


    # def setup(self):
    #     raise NotImplemented

    commands = {}


class DatePlugin(Plugin):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class TimePlugin(Plugin):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


