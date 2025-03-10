
move invoices.csv and organizations.csv to seeds.

Install duckdb (Mac OS)
```sh
brew install duckdb
duckdb my_database.db
```

To get started, install dependencies and run dbt:

```sh
poetry install --no-root  
poetry run dbt clean && dbt deps && dbt seed && dbt run && dbt test  
```


To simulate GitHub Actions locally, use Docker and act:
1) Start Docker Desktop.
2) Replace SLACK_WEBHOOK_URL
3) 
```sh
act -j dbt-run
```
Troubleshooting: On Mac with Apple Silicon, add the --container-architecture linux/amd64 flag.

Workflow Overview.

The workflow is scheduled to run dbt daily. After dbt runs, a Python script executes and sends alerts to Slack.



Improvements:
1) Use dbt snapshots (SCD2) instead of raw/seed data for staging models.
2) Add SQLFluff for SQL linting.
3) Write a CONTRIBUTING.md for best practices.
4) Run dbt in Docker (e.g., Airflow + Kubernetes).
5) Replace Slack alerts with Sentry or Datadog.
6) Switch materialization to incremental where possible; run full refresh only on weekends.
7) Use tags to organize dbt runs.
8) Restrict users from running dbt run on all models.
9) Add unit tests for dbt models.
10) Use dbt_date to standardize date formats.
11) Add CI tests before merging changes.
12) ...

Data is outdated, so alert is not sent. To test, remove if-else statements.

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices