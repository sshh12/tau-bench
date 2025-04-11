# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class SearchDirectFlight(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights = data["flights"]
        results = []
        for flight in flights.values():
            if flight["origin"] == origin and flight["destination"] == destination:
                if (
                    date in flight["dates"]
                    and flight["dates"][date]["status"] == "available"
                ):
                    # results add flight except dates, but add flight["datas"][date]
                    results.append({k: v for k, v in flight.items() if k != "dates"})
                    results[-1].update(flight["dates"][date])
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_direct_flight",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                        },
                        "destination": {
                            "type": "string",
                        },
                        "date": {
                            "type": "string",
                        },
                    },
                    "required": ["origin", "destination", "date"],
                },
            },
        }
