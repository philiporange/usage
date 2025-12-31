# Usage

A command-line tool that automatically generates comprehensive usage documentation for Python projects using AI. It analyzes your codebase and creates clear, example-rich documentation explaining how to use your project.

## Installation

```bash
pip install usage
```

## Quick Start

1. Set up your API configuration in a `.env` file:

```env
API_KEY=your_api_key_here
API_ENDPOINT=your_api_endpoint_here
```

2. Generate documentation for your project:

```bash
usage
```

This analyzes your Python project and generates a `USAGE.md` file with comprehensive documentation including code examples.

## Command-Line Options

```bash
usage [path]           # Generate docs for project at path (default: current directory)
usage --rebuild        # Force regeneration, overwriting existing USAGE.md
usage --print-only     # Print to stdout only, don't create USAGE.md file
```

## Caching

The tool automatically caches generated documentation in `USAGE.md` files. Subsequent runs will instantly return the cached version without making API calls. Use `--rebuild` when you've made code changes and need fresh documentation.

## How It Works

1. Uses `catenator` to concatenate all Python files in your project
2. Sends the concatenated code to an AI model via the `orac` library
3. Generates documentation with usage examples and code snippets
4. Saves output to `USAGE.md` for instant reuse

## Requirements

- Python 3.8+
- API credentials for OpenRouter or compatible AI service
- `.env` file with API configuration