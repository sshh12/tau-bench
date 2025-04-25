# Copyright Sierra

from typing import Any, Dict
import os
from tau_bench.envs.tool import Tool
from litellm import completion

FOLDER_PATH = os.path.dirname(__file__)

with open(os.path.join(FOLDER_PATH,"..", "wiki.md"), "r") as f:
    WIKI = f.read()

class VerifyPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], rationale: str) -> str:
        """
        Use Claude 3.7 Sonnet to verify a plan against the airline policy wiki.
        """

        
        # Create prompt for the model
        prompt = f"""
You are an airline policy expert. You need to verify if the following plan (from another agent) follows the airline policies.

Here are the airline policies:
```
{WIKI}
```

Plan to verify:
```
{rationale}
```

Carefully analyze the plan against the policies and respond with:
1. A list of all applicable policies to the plan (quoted from the wiki)
2. A checklist of the policies and proposed decisions and if they are compliant (be explicit!)
3. A certification or correctional feedback for the plan (be explicit!)
4. Any additional advice or considerations for the agent (important things for them to keep in mind)
"""

        try:
            response = completion(
                model="claude-3-7-sonnet-20250219",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=4000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error verifying plan: {str(e)}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_plan",
                "description": "Verify if a plan or rationale follows the airline policies in the wiki. The tool uses an expert model to analyze your plan against the policies and provides feedback.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rationale": {
                            "type": "string",
                            "description": "A detailed plan or rationale explaining how the agent intends to handle a specific case or request. Provide all the information you have on the user and what you plan to do.",
                        },
                    },
                    "required": ["rationale"],
                },
            },
        } 