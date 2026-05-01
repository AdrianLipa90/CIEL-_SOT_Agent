# ciel_news_reader.py — scripts/ciel_news_reader.py

## Identity
- **path:** `scripts/ciel_news_reader.py`
- **last_indexed:** `2026-05-01`

## Contents
- **classes:** Article
- **functions:** get_report_path, save_report, parse_date, fetch_feed, fetch_article_text, _keywords_match, generate_ciel_opinion, collect_articles, print_report, main

## Docstring
CIEL News Reader — wyszukuje najnowsze artykuły i generuje opinie w stylu CIEL.

Źródła: RSS feeds (BBC, Reuters, Al Jazeera, RMF24, PAP).
Bez API key. Oznaczenia epistemiczne: [FAKT] / [WYNIK] / [HIPOTEZA] / ≈odczucie.

Raporty zapisywane automatycznie do ~/Pulpit/NEWS/YYYY-MM-DD.AM.md (lub .PM.md)
