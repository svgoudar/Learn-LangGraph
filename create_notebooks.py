import json
import os

# Define all topics with their numbers
topics = [
    (9, "entry-node", "Entry Node", "An **Entry Node** is the starting point of execution in a graph. It's where the workflow begins."),
    (10, "exit-node", "Exit Node", "An **Exit Node** is a termination point where execution ends successfully."),
    (11, "terminal-node", "Terminal Node", "A **Terminal Node** is a node with no outgoing edges, representing an end state."),
    (12, "start-symbol", "Start Symbol", "A **Start Symbol** marks the initial state in state machines or formal grammars."),
    (13, "end-symbol", "End Symbol", "An **End Symbol** indicates the completion or acceptance state in formal systems."),
    (14, "compilation", "Compilation", "**Compilation** transforms a graph definition into an executable form, validating structure and optimizing execution."),
    (15, "execution-plan", "Execution Plan", "An **Execution Plan** is the ordered sequence of steps/nodes to be executed."),
    (16, "execution-engine", "Execution Engine", "An **Execution Engine** is the runtime system that executes the workflow by traversing the graph."),
    (17, "step-scheduler", "Step Scheduler", "A **Step Scheduler** determines which step to execute next in the workflow."),
    (18, "task-scheduler", "Task Scheduler", "A **Task Scheduler** manages the execution of multiple tasks, handling priorities and dependencies."),
    (19, "execution-context", "Execution Context", "**Execution Context** holds the state and environment information during graph execution."),
    (20, "execution-thread", "Execution Thread", "An **Execution Thread** represents an independent flow of execution, enabling concurrency."),
    (21, "execution-run", "Execution Run", "An **Execution Run** is a single instance of workflow execution from start to finish."),
    (22, "thread-id", "Thread ID", "A **Thread ID** uniquely identifies an execution thread in concurrent systems."),
    (23, "session", "Session", "A **Session** groups related execution runs and maintains state across multiple interactions."),
    (24, "run-id", "Run ID", "A **Run ID** is a unique identifier for a specific execution instance."),
    (25, "invocation", "Invocation", "**Invocation** is the act of triggering or calling a node or workflow for execution."),
    (26, "resume", "Resume", "**Resume** allows continuing execution from a paused or interrupted state."),
    (27, "interrupt", "Interrupt", "**Interrupt** temporarily halts execution, allowing for inspection or modification before continuing."),
    (28, "cancel", "Cancel", "**Cancel** terminates an ongoing execution and performs cleanup."),
    (29, "timeout", "Timeout", "**Timeout** enforces time limits on execution, aborting operations that exceed the threshold."),
]

def create_notebook(num, filename, title, description):
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# 1.{num} {title}\n\n{description}\n\n## Key Concepts\n- Understanding {title.lower()}\n- Practical implementation\n- LangGraph applications"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"# {title} Implementation\nimport networkx as nx\nimport matplotlib.pyplot as plt\nfrom typing import Dict, Any, List\n\nprint(f'{title} - Coming soon with practical examples')\nprint(f'This notebook covers: {title}')"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## Practical Example: {title} in Action\n\nHere we demonstrate {title.lower()} in a real workflow scenario."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"# Example implementation for {title}\n# This section demonstrates practical usage\n\nclass {title.replace(' ', '')}Example:\n    def __init__(self):\n        self.name = '{title}'\n    \n    def demonstrate(self):\n        print(f'Demonstrating: {{{filename}}}')\n        return True\n\nexample = {title.replace(' ', '')}Example()\nexample.demonstrate()"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    filepath = f"c:\\MyGithub\\Learn-LangGraph\\docs\\langgraph\\1-graph-execution-model\\{num:02d}-{filename}.ipynb"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    print(f"Created: {filepath}")

# Create all notebooks
for num, filename, title, description in topics:
    create_notebook(num, filename, title, description)

print(f"\n✓ Created {len(topics)} notebooks successfully!")
