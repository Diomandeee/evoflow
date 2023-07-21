from typing import Any
from evoflow.builder import EvolutionProcessBuilder
from evoflow.director import EvolutionProcessDirector


class EvolutionProcessContext:
    def __init__(self):
        self._context = {}

    @property
    def context(self) -> dict:
        return self._context

    @context.setter
    def context(self, value: dict):
        if not isinstance(value, dict):
            raise ValueError("context must be a dict.")
        self._context = value

    def add_context(self, key: str, value: Any) -> None:
        self._context[key] = value

    def remove_context(self, key: str) -> None:
        if key in self._context:
            del self._context[key]
        else:
            raise ValueError(f"Key '{key}' not found in context.")

    def clear_context(self) -> None:
        self._context.clear()



class EvolutionProcessRunner:
    def __init__(self, director: EvolutionProcessDirector):
        self._director = director

    @property
    def director(self) -> EvolutionProcessDirector:
        return self._director

    @director.setter
    def director(self, value: EvolutionProcessDirector):
        if not isinstance(value, EvolutionProcessDirector):
            raise ValueError("director must be an EvolutionProcessDirector object.")
        self._director = value

    def run_evoluation_process(self, context: dict) -> None:
        evolution_process = self._director.build_evolution_process()
        evolution_process.run_process(context)


class EvolutionProcessFacade:
    def __init__(self, builder: EvolutionProcessBuilder):
        self._context = EvolutionProcessContext()
        self._director = EvolutionProcessDirector(builder)
        self._runner = EvolutionProcessRunner(self._director)

    @property
    def context(self) -> EvolutionProcessContext:
        return self._context

    @property
    def director(self) -> EvolutionProcessDirector:
        return self._director

    @property
    def runner(self) -> EvolutionProcessRunner:
        return self._runner

    def run(self) -> None:
        self._runner.run_evoluation_process(self._context.context)


evo = EvolutionProcessFacade(EvolutionProcessBuilder())


evo.run()

print(evo.context.context)
