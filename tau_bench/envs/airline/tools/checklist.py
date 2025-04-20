# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class Checklist(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], checklist_verification: str) -> str:
        return "Checklist complete. Verify and proceed as needed."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "checklist",
                "description": "Use this tool before any modification action to systematically verify policy compliance. You MUST use this checklist tool before booking, modifying flights, updating baggage, upgrading cabin class, or updating passenger information to ensure all requirements are met.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "checklist_verification": {
                            "type": "string",
                            "description": "A detailed checklist verification that includes: 1) Specific rules that apply to the current request, 2) Verification that all required information is collected, 3) Confirmation that the planned action complies with all policies, 4) Analysis of any tool results for correctness.",
                        },
                    },
                    "required": ["checklist_verification"],
                },
            },
        } 