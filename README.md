# Usage

A simple tool for generating Python project documentation summaries using AI.

## Installation

```bash
pip install usage
```

## Usage

1. Set up your API configuration in a `.env` file:

```env
API_KEY=your_api_key_here
API_ENDPOINT=your_api_endpoint_here
```

2. Run the tool in your Python project directory:

```bash
usage
```

This will analyze your Python project and generate a comprehensive usage documentation summary.

## How it works

The tool uses `catenator` to concatenate all Python files in your project, then uses AI models through the `orac` library to generate documentation that explains how to use your project with code examples.

## Requirements

- Python 3.8+
- API credentials for the AI service
- `.env` file with API configuration

## License

CC0 - Public Domain