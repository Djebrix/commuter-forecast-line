# Commuter Forecast Line

[![Bounty](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Djebrix/commuter-forecast-line/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Djebrix/commuter-forecast-line/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather forecast, at most 140 characters, for a city that does
not exist — written to make a bored commuter smile on the way to work.

Competition: [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

## The line

> In Drizzlewick, light rain until 9am, then sunshine, 14 degrees, with a warm breeze that dries your socks before the office door.

## Run

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` is stdlib only, makes no network calls, and writes the single
forecast line to `<ENTRY_OUTPUT_DIR>/entry.txt` (default `/output`).
The line is asserted to be a single line of 1–140 characters.
