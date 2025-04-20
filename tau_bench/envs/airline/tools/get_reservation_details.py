# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class GetReservationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str) -> str:
        reservations = data["reservations"]
        if reservation_id in reservations:
            return json.dumps(reservations[reservation_id])
        return "Error: user not found"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Retrieves comprehensive information about a specific reservation using its ID. Use this tool to look up flight details, passenger information, payment history, baggage allowance, and insurance status for an existing reservation. Helpful when assessing modification options or responding to user inquiries about their booking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The reservation id, such as '8JX2WO'.",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }
