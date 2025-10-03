#!/usr/bin/env python3

"""
Command-line interface for the usage package.

This module provides the CLI entry point for the installed package.
"""

import sys
import argparse
from .main import main

def cli():
    """CLI entry point that parses arguments and calls the main function."""
    parser = argparse.ArgumentParser(description="Generate usage documentation for a Python project")
    parser.add_argument("path", nargs="?", default=".", help="Path to the Python project directory (default: current directory)")
    args = parser.parse_args()

    try:
        main(args.path)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    cli()