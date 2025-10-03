#!/usr/bin/env python3

"""
Main module for the usage package.

This module provides the core functionality for generating Python project
documentation summaries using AI.
"""

import os
import sys
from dotenv import load_dotenv
from catenator import Catenator
import orac
from orac import Prompt

# Load environment variables from .env file
load_dotenv()


def main(path="."):
    """Generate a usage summary for the Python project at the given path.

    Args:
        path (str): Path to the Python project directory to analyze. Defaults to current directory.
    """
    # Get API configuration from environment variables
    api_key = os.getenv('API_KEY')
    api_endpoint = os.getenv('API_ENDPOINT')

    if not api_key or not api_endpoint:
        print("Error: API_KEY and API_ENDPOINT must be set in .env file", file=sys.stderr)
        sys.exit(1)

    # Set the standard OpenRouter environment variable
    os.environ['OPENROUTER_API_KEY'] = api_key

    catenator = Catenator(path)
    catenation = catenator.catenate()

    # Initialize orac with default OpenRouter provider
    orac.init()
    llm = Prompt(os.path.join(os.path.dirname(__file__), 'prompts/python_summary.yaml'))

    output = llm.completion(code=catenation)
    print(output)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate usage documentation for a Python project")
    parser.add_argument("path", nargs="?", default=".", help="Path to the Python project directory (default: current directory)")
    args = parser.parse_args()
    sys.exit(main(args.path))