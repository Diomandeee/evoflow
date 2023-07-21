from typing import Dict, List, Union


class Dependencies:
    def __init__(self):
        self.dependencies: Dict[str, List[str]] = {}

    def add_dependency(
        self, step_name: str, dependencies: Union[str, List[str]]
    ) -> None:
        """
        Add dependencies for a step.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        if isinstance(dependencies, str):
            dependencies = [dependencies]
        elif not isinstance(dependencies, list):
            raise TypeError("Dependencies must be a string or a list of strings.")
        if step_name in self.dependencies:
            raise ValueError(f"Dependencies for step '{step_name}' already exist.")
        for dependency in dependencies:
            if not isinstance(dependency, str):
                raise TypeError("Dependencies must be strings.")
            if dependency not in self.dependencies:
                raise ValueError(f"Dependency '{dependency}' does not exist.")
        self.dependencies[step_name] = dependencies

    def get_dependencies(self, step_name: str) -> List[str]:
        """
        Get the dependencies of a step.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        return self.dependencies.get(step_name, [])

    def has_dependencies(self, step_name: str) -> bool:
        """
        Check if a step has dependencies.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        return step_name in self.dependencies

    def get_dependents(self, step_name: str) -> List[str]:
        """
        Get the steps that depend on the given step.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        dependents = []
        for name, dependencies in self.dependencies.items():
            if step_name in dependencies:
                dependents.append(name)
        return dependents

    def has_dependencies(self, step_name: str) -> bool:
        """
        Check if a step has dependencies.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        return step_name in self.dependencies

    def remove_dependencies(self, step_name: str) -> None:
        """
        Remove the dependencies for a step.
        """
        if not isinstance(step_name, str):
            raise TypeError("Step name must be a string.")
        if step_name not in self.dependencies:
            raise ValueError(f"No dependencies found for step '{step_name}'.")
        del self.dependencies[step_name]

    def get_all_steps(self) -> List[str]:
        """
        Get a list of all steps with dependencies.
        """
        return list(self.dependencies.keys())

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

    def print_dependencies(self) -> None:
        """
        Print the dependencies for all steps.
        """
        print("Dependencies:")
        for step, dependencies in self.dependencies.items():
            print(f"- {step}")
            if dependencies:
                print("  Dependents:")
                for dependency in dependencies:
                    print(f"  - {dependency}")

    def validate_dependencies(self) -> None:
        """
        Validate the dependencies to ensure there are no circular dependencies or missing dependencies.
        """
        visited = set()
        try:
            for step in self.dependencies:
                self._validate_dependencies_helper(step, visited, [])
        except Exception as e:
            raise ValueError("Dependency validation failed.") from e

    def _validate_dependencies_helper(
        self, step: str, visited: set, path: List[str]
    ) -> None:
        """
        Recursive helper method for validating dependencies.
        """
        visited.add(step)
        path.append(step)

        for dependency in self.get_dependencies(step):
            if dependency in path:
                raise ValueError(f"Circular dependency detected: {path + [dependency]}")
            if dependency not in visited:
                self._validate_dependencies_helper(dependency, visited, path)

        path.pop()

    def get_step_execution_order(self) -> List[str]:
        """
        Get the order of step execution based on the dependencies.
        """
        self.validate_dependencies()
        execution_order = []
        visited = set()

        def dfs(step):
            visited.add(step)
            for dependency in self.get_dependencies(step):
                if dependency not in visited:
                    dfs(dependency)
            execution_order.append(step)

        for step in self.dependencies:
            if step not in visited:
                dfs(step)

        return execution_order
