from openbench.config import BenchmarkMetadata

# Metadata for this eval
__metadata__ = BenchmarkMetadata(
    name="GPQA Diamond",
    description="Graduate-level Google-Proof Q&A in biology, chemistry, and physics",
    category="science",
    tags=["multiple-choice", "science", "graduate-level", "expert-validated"],
    module_path="gpqa.gpqa",
    function_name="gpqa_diamond",
)
