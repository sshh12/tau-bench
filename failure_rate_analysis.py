#!/usr/bin/env python3
# Copyright Sierra

import json
import argparse
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import importlib.util
import sys
import os


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze failure rates by task ID")
    parser.add_argument("--results-path", type=str, required=True, help="Path to the results JSON file")
    parser.add_argument("--output-path", type=str, help="Path to the output file. If not provided, results will be printed to stdout")
    parser.add_argument("--min-attempts", type=int, default=1, help="Minimum number of attempts required for a task to be included")
    parser.add_argument("--env", type=str, choices=["airline", "retail"], help="The environment to load tasks from")
    return parser.parse_args()


def load_tasks(env: str) -> Optional[List]:
    """Load tasks from the appropriate module based on environment"""
    if env == "airline":
        module_path = os.path.join("tau_bench", "envs", "airline", "tasks_test.py")
        module_name = "tau_bench.envs.airline.tasks_test"
    elif env == "retail":
        module_path = os.path.join("tau_bench", "envs", "retail", "tasks_test.py")
        module_name = "tau_bench.envs.retail.tasks_test"
    else:
        return None
    
    try:
        # Try to import the module directly
        module = __import__(module_name, fromlist=["TASKS"])
        return module.TASKS
    except ImportError:
        # If direct import fails, try to load the module from the file path
        try:
            if os.path.exists(module_path):
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return getattr(module, "TASKS", None) or getattr(module, "TASKS_TEST", None)
        except Exception as e:
            print(f"Error loading tasks: {e}")
    
    return None


def analyze_failure_rates(results_path: str, tasks: Optional[List] = None, min_attempts: int = 1) -> List[Tuple]:
    """
    Analyze failure rates by task ID
    
    Args:
        results_path: Path to the results JSON file
        tasks: Optional list of tasks to get user IDs from
        min_attempts: Minimum number of attempts required for a task to be included
        
    Returns:
        List of tuples (task_id, failure_rate, failures, attempts, user_id) sorted by failure rate in descending order
    """
    with open(results_path, "r") as f:
        results = json.load(f)
    
    # Count attempts and failures by task ID
    attempts_by_task = defaultdict(int)
    failures_by_task = defaultdict(int)
    
    for result in results:
        task_id = result["task_id"]
        attempts_by_task[task_id] += 1
        if result["reward"] <= 1e-3:  # Same failure criterion as in auto_error_identification.py
            failures_by_task[task_id] += 1
    
    # Calculate failure rates and filter by minimum attempts
    failure_rates = []
    for task_id, attempts in attempts_by_task.items():
        if attempts >= min_attempts:
            failures = failures_by_task[task_id]
            failure_rate = failures / attempts
            
            # Get user_id from task if available
            user_id = None
            if tasks and 0 <= task_id < len(tasks):
                user_id = getattr(tasks[task_id], "user_id", None)
            
            failure_rates.append((task_id, failure_rate, failures, attempts, user_id))
    
    # Sort by failure rate in descending order
    failure_rates.sort(key=lambda x: x[1], reverse=True)
    
    return failure_rates


def format_results(failure_rates: List[Tuple]) -> str:
    """Format the results as a string"""
    if failure_rates and len(failure_rates[0]) > 4:  # Check if we have user_id
        lines = ["task_id,failure_rate,failures,attempts,user_id"]
        for task_id, failure_rate, failures, attempts, user_id in failure_rates:
            user_id_str = user_id if user_id else ""
            lines.append(f"{task_id},{failure_rate:.4f},{failures},{attempts},{user_id_str}")
    else:
        lines = ["task_id,failure_rate,failures,attempts"]
        for task_id, failure_rate, failures, attempts, *_ in failure_rates:
            lines.append(f"{task_id},{failure_rate:.4f},{failures},{attempts}")
    
    return "\n".join(lines)


def main() -> None:
    args = get_args()
    
    # Load tasks if environment is specified
    tasks = None
    if args.env:
        tasks = load_tasks(args.env)
        if tasks:
            print(f"Loaded {len(tasks)} tasks from {args.env} environment")
        else:
            print(f"Warning: Could not load tasks from {args.env} environment")
    
    failure_rates = analyze_failure_rates(args.results_path, tasks, args.min_attempts)
    
    result_str = format_results(failure_rates)
    
    if args.output_path:
        with open(args.output_path, "w") as f:
            f.write(result_str)
        print(f"Results saved to {args.output_path}")
    else:
        print(result_str)
        
    # Print summary
    total_tasks = len(failure_rates)
    if total_tasks == 0:
        print("\nNo tasks met the minimum attempts criteria.")
        return
        
    perfect_tasks = sum(1 for _, failure_rate, _, _, *_ in failure_rates if failure_rate == 0)
    always_failing_tasks = sum(1 for _, failure_rate, _, _, *_ in failure_rates if failure_rate == 1)
    
    print(f"\nSummary:")
    print(f"Total tasks with at least {args.min_attempts} attempts: {total_tasks}")
    print(f"Tasks with 0% failure rate: {perfect_tasks} ({perfect_tasks/total_tasks*100:.2f}%)")
    print(f"Tasks with 100% failure rate: {always_failing_tasks} ({always_failing_tasks/total_tasks*100:.2f}%)")


if __name__ == "__main__":
    main() 