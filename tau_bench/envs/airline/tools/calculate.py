# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class Calculate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], expression: str) -> str:
        if not all(char in "0123456789+-*/(). " for char in expression):
            return "Error: invalid characters in expression"
        try:
            return str(round(float(eval(expression, {"__builtins__": None}, {})), 2))
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                        },
                    },
                    "required": ["expression"],
                },
            },
        }
