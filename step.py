from typing import List, Optional, Any
from enum import Enum
import logging
from evoflow.dependencies import Dependencies


class Status(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    SUCCESS = 3
    FAILURE = 4
    TIMEOUT = 5
    ROLLED_BACK = 6


class Role(Enum):
    VD = "Vocabulary Deconstructor (VD)"
    TS = "Target Structure (TS)"
    PREVIOUS_OUTPUT = "Previous Output"
    NEXT_OUTPUT = "Next Output"
    IDEA_GENERATION = "Idea Generation"
    FINALIZE = "Finalize"


class StepParameters:
    def __init__(self) -> None:
        self._parameters = {}

    def add_parameter(self, name: str, desc: str, default_value: Optional[str] = None):
        self._parameters[name] = {"desc": desc, "default_value": default_value}

    def get_parameter(self, name: str) -> Optional[str]:
        if name in self._parameters:
            return self._parameters[name]
        return None

    def get_all_parameters(self) -> List[str]:
        return list(self._parameters.keys())

    def validate_parameters(self, required_parameters: List[str]) -> bool:
        for parameter in required_parameters:
            if parameter not in self._parameters:
                return False
        return True

    def print_parameters(self, indent: int = 0) -> None:
        prefix = Step.INDENTATION * indent
        for parameter, details in self._parameters.items():
            print(
                f"{prefix}- {parameter}: {details['desc']}. Default value: {details['default_value']}"
            )


class Step:
    INDENTATION = "  "

    def __init__(
        self,
        name: str,
        description: str,
        roles: List[Role],
        substeps: Optional[List["Step"]] = None,
        dependencies: Optional[Dependencies] = None,
    ):
        self._name = name
        self._description = description
        self._roles = roles
        self._substeps = substeps
        self._dependencies = dependencies if dependencies else []
        self._parameters = StepParameters()
        self._result = None
        self._logger = logging.getLogger(__name__)
        self.condition = {
            "vd": None,
            "ts": None,
            "previous_output": None,
            "next_output": None,
            "idea_generation": None,
            "finalize": None,
        }

    def add_substep(self, substep: "Step") -> None:
        if self._substeps is None:
            self._substeps = []
        self._substeps.append(substep)

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def roles(self) -> List[Role]:
        return self._roles

    @property
    def substeps(self) -> Optional[List["Step"]]:
        return self._substeps

    @property
    def dependencies(self) -> Optional[Dependencies]:
        return self._dependencies

    @property
    def parameters(self) -> StepParameters:
        return self._parameters

    @property
    def result(self) -> Optional[str]:
        return self._result

    def set_result(self, value: Any) -> None:
        self._result = value

    def run_step(self, context: dict) -> None:
        if not self.validate_step():
            raise ValueError("Step validation failed.")
        try:
            # Placeholder method for step execution
            self._logger.info(f"Running step: {self.name}")
            # actual step execution
            self._logger.info(f"Finished running step: {self.name}")
        except Exception as e:
            self._logger.error(f"Error running step: {self.name}. {str(e)}")
            raise

    def validate_step(self) -> bool:
        # Check if dependencies have been met
        if self.dependencies:
            for dependency in self.dependencies:
                if dependency not in [step.name for step in self.substeps]:
                    print(f"Dependency {dependency} for step {self.name} is not met.")
                    return False
        # Check if required parameters are provided
        if self.parameters:
            required_parameters = self.parameters.get_all_parameters()
            if not self.parameters.validate_parameters(required_parameters):
                print(f"Validation failed for parameters in step {self.name}.")
                return False
        return True

    def print_step(self, indent: int = 0) -> None:
        prefix = self.INDENTATION * indent
        print(f"{prefix}- {self.name}: {self.description}")
        if self.roles:
            print(f"{prefix}{self.INDENTATION}Roles:")
            for role in self.roles:
                print(f"{prefix}{self.INDENTATION}{self.INDENTATION}- {role.value}")
        if self.result:
            print(f"{prefix}{self.INDENTATION}Result: {self.result}")
        if self.substeps:
            print(f"{prefix}{self.INDENTATION}Substeps:")
            for substep in self.substeps:
                substep.print_step(indent + 1)
                if self.dependencies:
                    print(
                        f"{prefix}{self.INDENTATION}Dependencies: {self.dependencies}"
                    )
                if self.parameters:
                    print(f"{prefix}{self.INDENTATION}Parameters:")
                    self.parameters.print_parameters(indent + 1)

    def rollback_step(self, context: dict) -> None:
        # Placeholder method for step rollback
        self._logger.info(f"Rolling back step: {self.name}")
        # actual step rollback
        self._logger.info(f"Finished rolling back step: {self.name}")

        if self.substeps:
            for substep in self.substeps:
                substep.rollback_step(context)

    def get_dependents(self) -> List[str]:
        dependents = []
        for dependency in self._dependencies:
            dependents.append(dependency)
        return dependents

    def get_dependencies(self) -> List[str]:
        return self._dependencies

    def get_all_dependents(self) -> List[str]:
        dependents = []
        for dependency in self._dependencies:
            dependents.append(dependency)
        for substep in self.substeps:
            dependents.extend(substep.get_all_dependents())
        return dependents

    def get_all_dependents(self, step_name: str) -> List[str]:
        """
        Get all the direct and indirect dependents of a step.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        dependents = self.get_dependents(step_name)
        for dependent in list(dependents):
            dependents.extend(self.get_all_dependents(dependent))
        return dependents
