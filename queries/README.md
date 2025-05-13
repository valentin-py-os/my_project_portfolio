# 📊 Hacker News SQL Analysis

This project contains SQL queries used to analyze posts from the Hacker News dataset.

## 🗂️ File Overview

- `hacker_news_analysis.sql` – Contains SQL queries to:
  - Categorize story sources (GitHub, Medium, NYT, etc.)
  - Count number of stories per source
  - Analyze story timestamps and scores by hour

## ▶️ How to Use

1. Load your Hacker News data into a SQL engine (e.g., SQLite, PostgreSQL, etc.).
2. Open and run the queries from `hacker_news_analysis.sql`.
3. Make sure your table is named `hacker_news` and includes at least the following columns:
   - `url`
   - `timestamp`
   - `score`

## 📎 Requirements

- SQL engine (tested with SQLite)
- A table named `hacker_news` with the necessary schema




