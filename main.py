"""One-line weather forecast for a city that does not exist.

Writes the forecast line to <ENTRY_OUTPUT_DIR>/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "In Drizzlewick, light rain until 9am, then sunshine, 14 degrees, "
    "with a warm breeze that dries your socks before the office door."
)

assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
assert LINE.strip() == LINE and "\n" not in LINE, "line must be a single line"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
