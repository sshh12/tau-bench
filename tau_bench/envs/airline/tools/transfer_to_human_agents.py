# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class TransferToHumanAgents(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        summary: str,
    ) -> str:
        return "Transfer successful"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Escalates the conversation to a human customer service agent. Only use this tool in specific circumstances: (1) when the user explicitly requests to speak with a human, (2) when you encounter complex policy exceptions that require human approval, (3) when handling unusual reservation changes that you cannot process with your tools, or (4) when troubleshooting technical issues with the booking system. Always include a detailed summary of the user's issue and what has been attempted so far.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "A summary of the user's issue.",
                        },
                    },
                    "required": [
                        "summary",
                    ],
                },
            },
        }
