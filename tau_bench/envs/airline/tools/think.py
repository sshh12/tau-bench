# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class Think(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thought: str) -> str:
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "An internal reasoning tool that allows structured analysis of complex situations without affecting the reservation system. Use this tool to organize your thoughts when planning multi-step processes, comparing flight options, calculating complex price differences, or working through policy-based decisions. The thought content is logged but not shown to users, making it ideal for breaking down complex tasks or reasoning through edge cases.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {
                            "type": "string",
                            "description": "A thought to think about.",
                        },
                    },
                    "required": ["thought"],
                },
            },
        }
