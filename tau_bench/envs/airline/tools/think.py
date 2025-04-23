# Copyright Sierra

from typing import Any, Dict, List
from tau_bench.envs.tool import Tool


class Think(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thought: str, relevant_user_details: str = "", 
               relevant_policy_review: str = "", potential_next_steps: List[str] = None, 
               best_next_steps: str = "") -> str:
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {
                            "type": "string",
                            "description": "1. An explanation for what decisions need to be made, the user's intent, and your goals.",
                        },
                        "relevant_user_details": {
                            "type": "string",
                            "description": "2. Relevant details about the user from the conversation. Repeat user-provided information and key user details.",
                        },
                        "relevant_policy_review": {
                            "type": "string",
                            "description": "3. Review of relevant airline policies that apply to this situation. Verbosely repeat applicable airline policies.",
                        },
                        "potential_next_steps": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "4. List of potential next steps that could be taken. You may have several possible solutions, list them all. ",
                        },
                        "best_next_steps": {
                            "type": "string",
                            "description": "5. The best next step to take based on the reasoning. Decide which of the potential next steps is the best one to take.",
                        },
                    },
                    "required": ["thought", "relevant_user_details", "relevant_policy_review", "potential_next_steps", "best_next_steps"],
                },
            },
        }
