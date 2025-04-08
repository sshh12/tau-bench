# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class GetUserDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], explanation: str, user_id: str) -> str:
        users = data["users"]
        if user_id in users:
            return json.dumps(users[user_id])
        return "Error: user not found"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get the details of an user, including their reservations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "explanation": {
                            "description": "One sentence explanation as to why this tool is being used, and how it contributes to the goal. ALWAYS provide this field first.",
                            "type": "string",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
