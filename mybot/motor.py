import traitlets
from traitlets.config.configurable import Configurable

class Motor(Configurable):
    value = traitlets.Float()

    def __init__(self, *args, **kwargs):
        super(Motor, self).__init__(*args, **kwargs)  # initializes traitle

    @traitlets.observe('value')
    def _observe_value(self, change):
        self._write_value(change['new'])
        print(self.value)

    def _write_value(self, value):
        self.value = value