# Copyright Sierra

import os

FOLDER_PATH = os.path.dirname(__file__)

with open(os.path.join(FOLDER_PATH, "wiki.md"), "r") as f:
    WIKI = f.read() + "\n\n" + """
## Policy Advice

Before taking any action (sending cert, updating data, etc), you MUST seek policy advice using the policy_advice tool.

Provide detailed context about the user's situation, request, or problem to receive guidance on relevant policies.
""".strip()
