from openbench.config import BenchmarkMetadata

# Metadata for this eval
__metadata__ = BenchmarkMetadata(
    name="SimpleQA",
    description="Measuring short-form factuality in large language models with simple Q&A pairs",
    category="factuality",
    tags=["factuality", "question-answering", "graded", "model-based-scoring"],
    module_path="simpleqa.simpleqa",
    function_name="simpleqa",
)
