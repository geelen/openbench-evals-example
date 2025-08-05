from inspect_ai import Task, task, Epochs
from inspect_ai.model import GenerateConfig
from inspect_ai.solver import generate
from typing import Optional
from openbench.utils.imports import import_module_from_same_dir

# Import the required modules
dataset_module = import_module_from_same_dir(__file__, "dataset")
scorer_module = import_module_from_same_dir(__file__, "scorer")
get_humaneval_dataset = dataset_module.get_humaneval_dataset
verify = scorer_module.verify


# Adapted from https://github.com/UKGovernmentBEIS/inspect_evals
@task
def humaneval(instruction_prompt: Optional[str] = None) -> Task:
    """
    Inspect Task implementation for the HumanEval benchmark.
    Args:
        instruction_prompt (str, optional): The prompt to prepend to the code problem.
            If None, uses the default HumanEval instruction.
    Returns:
        Task: The configured HumanEval task.
    """
    epochs_count = 5
    reducer_list = ["mean", "pass_at_1", "pass_at_2", "pass_at_5"]

    dataset = (
        get_humaneval_dataset()
        if instruction_prompt is None
        else get_humaneval_dataset(instruction_prompt=instruction_prompt)
    )

    return Task(
        dataset=dataset,
        solver=generate(),
        scorer=verify(),
        sandbox="local",
        config=GenerateConfig(
            temperature=0.5,
        ),
        epochs=Epochs(epochs_count, reducer=reducer_list),
    )
