from evoflow.template import EvolutionTemplates
from evoflow.process import Step
from evoflow.step import Role
from evoflow.parallel import EvolutionProcess


class EvolutionProcessBuilder:
    def __init__(self):
        self._evolution_process = EvolutionProcess([])
        self._evolution_templates = EvolutionTemplates

    @property
    def evolution_process(self) -> EvolutionProcess:
        return self._evolution_process

    @evolution_process.setter
    def evolution_process(self, value: EvolutionProcess):
        if not isinstance(value, EvolutionProcess):
            raise ValueError("evolution_process must be an EvolutionProcess object.")
        self._evolution_process = value

    @property
    def evolution_templates(self) -> EvolutionTemplates:
        return self._evolution_templates

    @evolution_templates.setter
    def evolution_templates(self, value: EvolutionTemplates):
        if not isinstance(value, EvolutionTemplates):
            raise ValueError(
                "evolution_templates must be an EvolutionTemplates object."
            )
        self._evolution_templates = value

    def build(self) -> EvolutionProcess:
        # Initialize an empty list to hold all steps in the process
        process_steps = []

        # Iterate over all templates in EvolutionTemplates
        for template_name, template in self._evolution_templates.__members__.items():
            # Get the description of the current template
            template_description = template.value

            # Initialize an empty list to hold the roles associated with this template
            associated_roles = []

            # The first step in the process is always the Idea Generation step {prompt}\n"

            if template_name == "IDEA_GENERATION_PROMPT_TMPL":
                associated_roles.append(Role.IDEA_GENERATION)
                process_steps.append(
                    Step(template_name, template_description, associated_roles)
                )
                continue

            # The last step in the process is always the Finalize step {prompt}\n"

            if template_name == "FINALIZE_PROMPT_TMPL":
                associated_roles.append(Role.FINALIZE)
                process_steps.append(
                    Step(template_name, template_description, associated_roles)
                )
                continue

            # Check if the Vocabulary Deconstructor's context or Target Structure's context are needed in this template
            # If so, add the appropriate roles to the associated_roles list
            if "{vd_context_str}" in template_description:
                associated_roles.append(Role.VD)
            if "{ts_context_str}" in template_description:
                associated_roles.append(Role.TS)

            # Create a new step for this template and add it to the process_steps list
            process_steps.append(
                Step(template_name, template_description, associated_roles)
            )

        # Create a new EvolutionProcess object with the process_steps list and return it
        self._evolution_process = EvolutionProcess(process_steps)
        return self._evolution_process
