# Copyright Sierra

import json
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool


class UpdateReservationPassengers(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str,
        passengers: List[Dict[str, Any]],
    ) -> str:
        reservations = data["reservations"]
        if reservation_id not in reservations:
            return "Error: reservation not found"
        reservation = reservations[reservation_id]
        if len(passengers) != len(reservation["passengers"]):
            return "Error: number of passengers does not match"
        reservation["passengers"] = passengers
        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_passengers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                        },
                        "passengers": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {
                                        "type": "string",
                                    },
                                    "last_name": {
                                        "type": "string",
                                    },
                                    "dob": {
                                        "type": "string",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                    },
                    "required": ["reservation_id", "passengers"],
                },
            },
        }
