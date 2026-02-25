#!/usr/bin/env python

# Example Tests
import sys
import os
import asyncio

PROJECT_ROOT = os.getcwd()
print(PROJECT_ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.logger import *
from src.graph.Compile_graph import run

if __name__ == "__main__":
    asyncio.run(run("State of Multimodal LLMs in 2026"))

