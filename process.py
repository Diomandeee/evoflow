from typing import List, Optional
import logging
import time
from evoflow.step import Step


class Process:
    def __init__(self, steps: List[Step]) -> None:
        self._steps = steps
        self._current_step = None
        self._completed_steps = []
        self._logger = logging.getLogger(__name__)

    @property
    def steps(self) -> List[Step]:
        return self._steps

    @property
    def current_step(self) -> Step:
        return self._current_step

    @property
    def completed_steps(self) -> List[str]:
        return self._completed_steps

    def start_process(self) -> None:
        self._current_step = self._get_next_executable_step()

    def _get_next_executable_step(self) -> Optional[Step]:
        for step in self._steps:
            if (
                step.name not in self._completed_steps
                and self._check_dependencies(step)
                and self._check_condition(step)
            ):
                return step
        return None

    def get_all_steps(self) -> List[Step]:
        return self._steps

    def next_step(self) -> None:
        if self._current_step:
            self.completed_steps.append(self._current_step.name)
            self._current_step = self._get_next_executable_step()
            if self._current_step:
                self._logger.info(f"Next step: {self._current_step.name}")
            else:
                self._logger.info("Process completed")
        else:
            raise ValueError("Process has already completed")

    def previous_step(self) -> None:
        if self._current_step:
            self.completed_steps.remove(self._current_step.name)
            self._current_step = self._get_next_executable_step()
            if self._current_step:
                self._logger.info(f"Previous step: {self._current_step.name}")
            else:
                self._logger.info("Process has not started yet")
        else:
            raise ValueError("Process has not started yet")

    def go_to_step(self, step_name: str) -> None:
        for step in self._steps:
            if step.name == step_name:
                if step.name in self.completed_steps:
                    self.completed_steps.remove(step.name)
                self._current_step = step
                self._logger.info(f"Jumped to step: {step.name}")
                return
        raise ValueError(f"No step named '{step_name}' found")

    def _get_next_executable_step(self) -> Optional[Step]:
        for step in self._steps:
            if (
                step.name not in self._completed_steps
                and self._check_dependencies(step)
                and self._check_condition(step)
            ):
                return step
        return None

    def _check_dependencies(self, step: Step) -> bool:
        dependencies = step.get_dependencies()
        for dependency in dependencies:
            if dependency not in self._completed_steps:
                return False
        return True

    def _check_condition(self, step: Step) -> bool:
        return step.condition

    def run_current_step(self, context: dict) -> None:
        if self._current_step:
            if not self._current_step.validate_step():
                raise ValueError(f"Step '{self._current_step.name}' failed validation")

            retries = self._current_step.retries
            retry_interval = self._current_step.retry_interval
            retry_count = 0

            while retries >= 0:
                try:
                    self._logger.info(f"Running step: {self._current_step.name}")
                    self._current_step.run_step(context)
                    self.completed_steps.append(self._current_step.name)
                    self._logger.info(
                        f"Step '{self._current_step.name}' execution completed"
                    )
                    return
                except Exception as e:
                    self._logger.error(
                        f"Error running step '{self._current_step.name}': {str(e)}"
                    )
                    retry_count += 1
                    if retry_count > retries:
                        raise ValueError(
                            f"Step '{self._current_step.name}' failed after {retry_count} retries"
                        )
                    self._logger.info(
                        f"Retrying step '{self._current_step.name}' in {retry_interval} seconds..."
                    )
                    time.sleep(retry_interval)
                    retries -= 1
        else:
            raise ValueError("Process has already completed")

    def print_current_step(self) -> None:
        if self._current_step:
            self._current_step.print_step()
        else:
            raise ValueError("Process has already completed")
