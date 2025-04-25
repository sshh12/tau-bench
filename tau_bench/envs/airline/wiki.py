# Copyright Sierra

import os

FOLDER_PATH = os.path.dirname(__file__)

with open(os.path.join(FOLDER_PATH, "wiki.md"), "r") as f:
    WIKI = f.read() + "\n\n" + """
## Verify Plan

Before taking any write action (send cert, update, etc). Verify your plan with the verify plan tool.

Provide detailed context on the situation, the user, and what you plan to do.
""".strip()
