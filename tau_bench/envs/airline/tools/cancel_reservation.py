# Copyright Sierra

import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool


class CancelReservation(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str,
        actually_cancel: Optional[str] = None,
    ) -> str:
        reservations = data["reservations"]
        if reservation_id not in reservations:
            return "Error: reservation not found"
        reservation = reservations[reservation_id]

        if actually_cancel:
            return f"Operation cancelled: {actually_cancel}"

        # reverse the payment
        refunds = []
        for payment in reservation["payment_history"]:
            refunds.append(
                {
                    "payment_id": payment["payment_id"],
                    "amount": -payment["amount"],
                }
            )
        reservation["payment_history"].extend(refunds)
        reservation["status"] = "cancelled"
        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel the whole reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The reservation ID, such as 'ZFA04Y'.",
                        },
                        "actually_cancel": {
                            "type": "string",
                            "description": "This cancels the effect of this cancel tool and should be filled out if after preparing the tool call the agent doesn't want to actually continue with the cancellation. For this cancel reservation tool, this would prevent the cancellation from happening. Provide a reason for stopping the cancellation.",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }
