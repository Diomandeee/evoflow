import concurrent.futures
from typing import List, Any
from evoflow.process import Process
from evoflow.step import Step


class EvolutionProcess(Process):
    def __init__(self, steps: List[Step], max_workers: int = 4) -> None:
        super().__init__(steps)
        self._max_workers = max_workers

    def run_process(self, context: dict) -> None:
        self.start_process()
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self._max_workers
        ) as executor:
            while self._current_step:
                self.print_current_step()
                self.run_current_step(context, executor)
                self.next_step()

    def run_current_step(
        self, context: dict, executor: concurrent.futures.ThreadPoolExecutor
    ) -> None:
        if self._current_step:
            if not self._current_step.validate_step():
                raise ValueError(f"Step '{self._current_step.name}' failed validation")

            dependent_results = self._execute_dependent_steps(context, executor)

            try:
                result = self._execute_step(
                    self._current_step, context, dependent_results
                )
                self._current_step.set_result(result)
                self.completed_steps.append(self._current_step.name)
            except Exception as e:
                self._logger.error(
                    f"Error running step '{self._current_step.name}': {str(e)}"
                )
                self._handle_step_failure(self._current_step)
        else:
            raise ValueError("Process has already completed")

    def _execute_dependent_steps(
        self, context: dict, executor: concurrent.futures.ThreadPoolExecutor
    ) -> List:
        dependent_results = []
        dependencies = self._current_step.dependencies

        if dependencies:
            dependent_steps = [
                step for step in self._steps if step.name in dependencies
            ]
            dependent_futures = [
                executor.submit(self._execute_step, step, context)
                for step in dependent_steps
            ]

            for future in concurrent.futures.as_completed(dependent_futures):
                dependent_results.append(future.result())
        return dependent_results

    def _execute_step(self, step: Step, context: dict, dependent_results: List) -> Any:
        if dependent_results:
            return step.run_step(context, *dependent_results)
        else:
            return step.run_step(context)

    def _handle_step_failure(self, step: Step) -> None:
        if step.name == "IDEA_GENERATION_PROMPT_TMPL":
            self._logger.info("Idea Generation step failed. Exiting process.")
            exit(1)
        else:
            self._logger.info("Step failed. Rolling back to previous step.")
            self.rollback()

    def rollback(self) -> None:
        if not self.completed_steps:
            raise ValueError("No steps have been completed in the process")

        rollback_steps = []

        # Find rollback steps for completed steps
        for step in reversed(self.completed_steps):
            if step.rollback_step:
                rollback_steps.append(step.rollback_step)

        # Execute rollback steps in reverse order
        for step in reversed(rollback_steps):
            if step:
                try:
                    result = self._execute_step(step, context={}, dependent_results=[])
                    step.set_result(result)

                except Exception as e:
                    self._logger.error(f"Error executing rollback step: {str(e)}")

        self.completed_steps.clear()

    def print_current_step(self) -> None:
        if self._current_step:
            self._current_step.print_step()
        else:
            raise ValueError("Process has already completed")
