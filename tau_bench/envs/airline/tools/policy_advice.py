# Copyright Sierra

from typing import Any, Dict
import os
from tau_bench.envs.tool import Tool
from litellm import completion

FOLDER_PATH = os.path.dirname(__file__)

with open(os.path.join(FOLDER_PATH,"..", "wiki.md"), "r") as f:
    WIKI = f.read()

class PolicyAdvice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_context: str) -> str:
        """
        Use Claude 3.7 Sonnet to provide policy advice based on user context before planning.
        """

        
        # Create prompt for the model
        prompt = f"""
You are an airline policy expert. You need to provide guidance on relevant policies based on the user's context.

Here are the airline policies:
```
{WIKI}
```

User context:
```
{user_context}
```

Carefully analyze the user context against the policies and respond with:
1. A list of all applicable policies to this situation (quoted from the wiki)
2. Clear guidance on what approaches are allowed and not allowed in this situation
3. Specific policy-based recommendations the agent should follow
4. Any important considerations or edge cases the agent should be aware of
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
            return f"Error providing policy advice: {str(e)}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "policy_advice",
                "description": "Get advice on relevant airline policies by a certified expert before making a plan or taking an important action. Provide user context to receive guidance on how to handle the situation within policy constraints.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_context": {
                            "type": "string",
                            "description": "Detailed information about the user's situation, request, or problem that requires policy guidance. Include all relevant details about the user and their circumstances.",
                        },
                    },
                    "required": ["user_context"],
                },
            },
        } 