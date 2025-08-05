# OpenBench Evals Example

This repository contains example implementations of three evaluation benchmarks for the [OpenBench](https://github.com/OpenBenchAI/openbench) project:

- **GPQA** - Graduate-level Google-proof Q&A benchmark
- **HumanEval** - Code generation benchmark for Python programming
- **SimpleQA** - Factual question answering benchmark

These implementations demonstrate how to create custom evaluations using the OpenBench framework built on Inspect AI.

## Structure

```
├── gpqa/           # GPQA evaluation implementation
├── humaneval/      # HumanEval evaluation implementation  
├── simpleqa/       # SimpleQA evaluation implementation
└── README.md       # This file
```

Each evaluation directory contains:
- `__init__.py` - Package initialization
- `dataset.py` - Dataset loading and preprocessing
- `{eval_name}.py` - Main evaluation task definition
- `scorer.py` - Custom scoring logic (where applicable)

## Usage Instructions

Uses the `bench` command from [openbench](https://github.com/groq/openbench):

```bash
bench eval ./gpqa --model groq/moonshotai/kimi-k2-instruct --limit 10
bench eval ./simpleqa --model groq/moonshotai/kimi-k2-instruct --limit 10
bench eval ./humaneval --model groq/moonshotai/kimi-k2-instruct --limit 10 --epochs 5
```

Use `uvx` to get `bench` without installing it:

```
uvx --from git+https://github.com/groq/openbench bench eval ./gpqa --model groq/moonshotai/kimi-k2-instruct --limit 10
```

Or install it:

```bash
uv venv
source .venv/bin/activate
uv pip install openbench
```

## Features

- **Provider-agnostic**: Works with 15+ model providers through Inspect AI
- **Modular design**: Shared components and utilities reduce code duplication
- **Type-safe**: Full type hints throughout the codebase
- **Extensible**: Easy to modify and extend for custom use cases

## Requirements

- Python 3.8+
- OpenBench package
- Inspect AI framework

## Contributing

These are example implementations. For the main OpenBench project, please visit [OpenBench](https://github.com/OpenBenchAI/openbench).

## License

MIT License - see the main OpenBench project for details.
