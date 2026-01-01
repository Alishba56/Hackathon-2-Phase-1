#!/usr/bin/env python3
"""
Todo Application - Main Entry Point

This is the main entry point for the in-memory todo console application.
It initializes the application components and starts the main loop.
"""

from cli import TodoCLI


def main():
    """Main application entry point"""
    print("Welcome to the Todo Application!")

    # Initialize the CLI interface
    cli = TodoCLI()

    # Start the main application loop
    cli.run()


if __name__ == "__main__":
    main()