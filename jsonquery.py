#!/usr/bin/env python3

#By Suyash Jain

import json
import re
import argparse
from typing import Any, List


def match_pattern(pattern: str, text: Any, use_regex: bool) -> bool:
    if pattern is None:
        return True
    if text is None:
        return False

    text = str(text)

    if use_regex:
        return re.search(pattern, text) is not None
    else:
        return pattern == text


def object_matches(obj: Any, key_pattern: str, value_pattern: str, use_regex: bool) -> bool:
    """
    Recursively checks if any key/value inside the object matches criteria
    """

    if isinstance(obj, dict):
        for k, v in obj.items():
            key_match = match_pattern(key_pattern, k, use_regex)
            value_match = match_pattern(value_pattern, v, use_regex)

            if key_match and value_match:
                return True

            if object_matches(v, key_pattern, value_pattern, use_regex):
                return True

    elif isinstance(obj, list):
        for item in obj:
            if object_matches(item, key_pattern, value_pattern, use_regex):
                return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Search JSON and return matched + non-matched objects"
    )
    parser.add_argument("file", help="Path to JSON file")
    parser.add_argument("--key", help="Key to search (exact or regex)")
    parser.add_argument("--value", help="Value to search (exact or regex)")
    parser.add_argument("--regex", action="store_true",
                        help="Enable regex search")
    parser.add_argument("--count-only", action="store_true",
                        help="Return only counts")
    parser.add_argument("--show-matched", action="store_true",
                        help="Show only matched data")
    parser.add_argument("--show-unmatched", action="store_true",
                        help="Show only unmatched data")

    args = parser.parse_args()

    if not args.key and not args.value:
        print("You must provide --key or --value or both")
        return

    try:
        with open(args.file, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return

    if not isinstance(data, list):
        print("This version expects top-level JSON to be a list of objects.")
        return

    matched = []
    unmatched = []

    for obj in data:
        if object_matches(obj, args.key, args.value, args.regex):
            matched.append(obj)
        else:
            unmatched.append(obj)

    matched_count = len(matched)
    unmatched_count = len(unmatched)

    # COUNT ONLY MODE
    if args.count_only:
        print(f"Matched Count   : {matched_count}")
        print(f"Unmatched Count : {unmatched_count}")
        print(f"Total Objects   : {len(data)}")
        return

    # PRINT RESULTS
    print(f"\nMatched Count   : {matched_count}")
    print(f"Unmatched Count : {unmatched_count}")
    print(f"Total Objects   : {len(data)}")

    if not args.show_unmatched:
        print("\n===== MATCHED OBJECTS =====")
        for idx, obj in enumerate(matched, 1):
            print(f"\nMatch {idx}")
            print(json.dumps(obj, indent=4))

    if not args.show_matched:
        print("\n===== UNMATCHED OBJECTS =====")
        for idx, obj in enumerate(unmatched, 1):
            print(f"\nUnmatched {idx}")
            print(json.dumps(obj, indent=4))


if __name__ == "__main__":
    main()
