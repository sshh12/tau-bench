# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class TransferToHumanAgents(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        explanation: str,
        summary: str,
    ) -> str:
        return "Transfer successful"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the user to a human agent, with a summary of the user's issue. Only transfer if the user explicitly asks for a human agent, or if the user's issue cannot be resolved by the agent with the available tools.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "explanation": {
                            "description": "One sentence explanation as to why this tool is being used, and how it contributes to the goal. ALWAYS provide this field first.",
                            "type": "string",
                        },
                         "summary": {
                            "type": "string",
                            "description": "A summary of the user's issue.",
                        },
                    },
                    "required": [
                        "summary"
                    ],
                },
            },
        }
