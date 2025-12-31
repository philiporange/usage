#!/usr/bin/env python3

"""
Main module for the usage package.

This module provides the core functionality for generating Python project
documentation summaries using AI. It supports caching generated documentation
to USAGE.md files to avoid redundant API calls.
"""

import os
import sys
from dotenv import load_dotenv
from catenator import Catenator
import orac
from orac import Prompt

# Load environment variables from .env file
load_dotenv()


def main(path=".", rebuild=False, print_only=False):
    """Generate a usage summary for the Python project at the given path.

    By default, this function will create a USAGE.md file in the target directory.
    If a USAGE.md file already exists, it will be returned unless --rebuild is specified.

    Args:
        path (str): Path to the Python project directory to analyze. Defaults to current directory.
        rebuild (bool): If True, regenerate and overwrite existing USAGE.md file. Defaults to False.
        print_only (bool): If True, only print to stdout without writing USAGE.md. Defaults to False.
    """
    # Resolve the absolute path
    abs_path = os.path.abspath(path)
    usage_file = os.path.join(abs_path, "USAGE.md")

    # Check for existing USAGE.md file (unless rebuild is requested)
    if not rebuild and not print_only and os.path.exists(usage_file):
        with open(usage_file, 'r') as f:
            output = f.read()
        print(output)
        return

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

    # Write to USAGE.md unless print_only is set
    if not print_only:
        with open(usage_file, 'w') as f:
            f.write(output)

    print(output)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate usage documentation for a Python project")
    parser.add_argument("path", nargs="?", default=".", help="Path to the Python project directory (default: current directory)")
    parser.add_argument("--rebuild", action="store_true", help="Regenerate and overwrite existing USAGE.md file")
    parser.add_argument("--print-only", action="store_true", help="Print to stdout only without creating USAGE.md file")
    args = parser.parse_args()
    main(args.path, rebuild=args.rebuild, print_only=args.print_only)