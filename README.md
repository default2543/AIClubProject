# AI Sports Betting Recommender

An AI Club prototype that scrapes an NFL team's recent win-loss records and
asks an LLM to analyze the trend and predict next season's record.

## How it works

1. `main.py` scrapes the Seattle Seahawks' records for 2019–2023 from
   [Pro Football Reference](https://www.pro-football-reference.com).
2. `ai.py` sends those records, plus an analyst prompt, to `gpt-4o-mini`
   through [OpenRouter](https://openrouter.ai).
3. The script prints a short trend analysis and a predicted win-loss record.

## Running it

```bash
pip install requests beautifulsoup4 openai
export OPENROUTER_API_KEY=your-key
python main.py
```

To analyze a different team, change `team_abbr` and `years` in `main.py`.

## Status

This is an early prototype. It covers one team and makes a season-level
prediction. It does not yet produce game-level betting recommendations.
