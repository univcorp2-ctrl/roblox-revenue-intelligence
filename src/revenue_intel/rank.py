from __future__ import annotations

import json
import sys

from .scoring import score_hypothesis


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "data/hypotheses.json"
    data = json.load(open(path, encoding="utf-8"))
    ranked = sorted(data, key=score_hypothesis, reverse=True)
    for index, item in enumerate(ranked, start=1):
        print(f"{index:>2}. {score_hypothesis(item):.3f}  {item['name']}")


if __name__ == "__main__":
    main()
