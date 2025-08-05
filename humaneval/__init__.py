from openbench.config import BenchmarkMetadata

# Metadata for this eval
__metadata__ = BenchmarkMetadata(
    name="HumanEval",
    description="Code generation benchmark with 164 programming problems",
    category="coding",
    tags=["coding", "generation", "execution", "functional-correctness"],
    module_path="humaneval.humaneval",
    function_name="humaneval",
)
