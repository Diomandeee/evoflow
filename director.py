from evoflow.parallel import EvolutionProcess
from evoflow.builder import EvolutionProcessBuilder


class EvolutionProcessDirector:
    def __init__(self, builder: EvolutionProcessBuilder):
        self._builder = builder

    @property
    def builder(self) -> EvolutionProcessBuilder:
        return self._builder

    @builder.setter
    def builder(self, value: EvolutionProcessBuilder):
        if not isinstance(value, EvolutionProcessBuilder):
            raise ValueError("builder must be an EvolutionProcessBuilder object.")
        self._builder = value

    def build_evolution_process(self) -> EvolutionProcess:
        return self._builder.build()
