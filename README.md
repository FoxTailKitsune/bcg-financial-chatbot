# BCG Financial Analysis Chatbot

A small Flask app built for the BCG GenAI job simulation on Forage. It answers questions about the 2023-2025 financial statements of Apple, Microsoft and Tesla using figures pulled from their 10-K filings.

## What it does

- Loads the figures extracted in `Forage BCG 10K Analysis.ipynb` (exported to `Forage BCG 10K Analysis.csv` and `.xlsx`).
- Matches the question against five financial intents: revenue growth, total revenue, net income change, net profit margin, and asset-to-liability ratio.
- Returns a plain-language answer with the reported numbers attached, for example:

> **Q:** What was the total revenue in 2025?
> **A:** In 2025, Apple reported the highest total revenue at $416.2 billion, followed by Microsoft at $281.7 billion, and Tesla at $94.8 billion.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Flask routes and the request handler |
| `chatbot.py` | Intent matching and the answer text |
| `templates/index.html` | Chat interface |
| `Forage BCG 10K Analysis.ipynb` | Extraction and ratio calculations over the filings |
| `Forage BCG 10K Analysis.csv` / `.xlsx` | The cleaned statement data |
| `documentation.ipynb` | Write-up of the approach |

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000.

## Notes

The answer logic is rule-based keyword matching, not a language model. Every number in a response comes from the extracted table, and the notebook shows where each one came from (revenue, net income, total assets and total liabilities by company and year).
