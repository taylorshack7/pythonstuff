Python projects & challenges I am working on/have completed... 

## Repo Structure

```
pythonstuff-main/
├── pythonproject-main/
│   ├── TechServiceAnalyzer_v1/
│   └── TechServiceAnalyzer_v2/
└── pythonchallenges-main/
    ├── BudgetApp/
    ├── DigitalDetox/
    └── tipCalculator/
```

## Projects

### TechServiceAnalyzer
Parses technician service data and models it into a normalized SQLite
database for querying dependencies between services, the incident times
associated with those services, and the results of different analysis
types (DFS, BFS, shortest path, etc.).

- **v1** — Initial working build. Read source data and wrote results to
  the console, proving the parsing and traversal logic end to end.
  Nothing was persisted, so there was no data lineage and each run's
  results were lost when the next one started.
- **v2** — **Current build.** Rebuilt around a normalized relational schema
  (designed as an ERD before implementation), persisting services,
  incidents, and analysis results as related entities with foreign keys.
  Runs are now stored rather than overwritten, so results are traceable
  over time and dependency questions can be answered directly in SQL
  instead of in code.

## Challenges

Short exercises from daily practice.

- **BudgetApp** — Expense tracking with category breakdowns
- **DigitalDetox** — Track user login behavior to qualif if digital detox goal met
- **tipCalculator** — Calculates tips for your bill. If bill split between party, totals expected tip for each member. 
