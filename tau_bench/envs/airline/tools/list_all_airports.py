# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class ListAllAirports(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        airports = [
            "SFO",
            "JFK",
            "LAX",
            "ORD",
            "DFW",
            "DEN",
            "SEA",
            "ATL",
            "MIA",
            "BOS",
            "PHX",
            "IAH",
            "LAS",
            "MCO",
            "EWR",
            "CLT",
            "MSP",
            "DTW",
            "PHL",
            "LGA",
        ]
        cities = [
            "San Francisco",
            "New York",
            "Los Angeles",
            "Chicago",
            "Dallas",
            "Denver",
            "Seattle",
            "Atlanta",
            "Miami",
            "Boston",
            "Phoenix",
            "Houston",
            "Las Vegas",
            "Orlando",
            "Newark",
            "Charlotte",
            "Minneapolis",
            "Detroit",
            "Philadelphia",
            "LaGuardia",
        ]
        return json.dumps({airport: city for airport, city in zip(airports, cities)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_airports",
                "description": "Returns a complete list of all airports served by the airline, with their IATA codes and corresponding city names. Use this tool when you need to verify airport codes, check if a specific destination is available, or present the user with all flight options. Returns a mapping of airport codes to city names.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
