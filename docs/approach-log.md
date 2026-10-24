# Approach log · Brief <LETTER> · Group <N>

One row per part of the work. At least two approaches in every row. Written when the choice is made, not afterwards; the commit timestamp is the proof. An approach you tried for twenty minutes and abandoned is the best kind of row. Keep the dead notebook cell and link to it.

The panel reads this file before it reads your notebooks. A panellist will cover the "chosen" column and ask you to choose again, aloud.

| # | Part of the work | Approaches considered (two at least) | Chosen | Why this, and not the others | What would have changed the choice | What happened when we tried it | Owner | Date |
|---|---|---|---|---|---|---|---|---|
| 0 | *Example: matching invoice ids to payment references* | *(a) Strip the prefix and match on digits. (b) Match on amount and date within two days. (c) Both, and keep the rows where they disagree.* | *(c)* | *(a) alone matched 91 percent and silently paired two invoices with one payment. (b) alone could not separate same-day same-amount visits. Together they flag what each misses.* | *A shared id in both feeds would have made (a) enough.* | *96 percent matched. The 4 percent became finance's list.* | *example* | *example* |
| 1 | Which table to count tests from | Count booking rows; sum n_tests; count result rows|Sum n_tests from valid bookings |A booking can contain multiple tests. Results measure tests run, while the plan is for booked test volume. |If the plan were based on completed lab tests, use results instead.If the plan were based on completed lab tests, use results instead. | The representative legacy file had 19,602 rows for 8,344 bookings; the Nova sample had 13,966 rows for 5,903 bookings. Counting rows would not count bookings. | chaitanya|23-10-2026 |
| 2 | How to define the period (first half, both years) | | | | | | | |
| 3 | Profiling: what to check in each table | | | | | | | |
| 4 | Duplicates: the identity rule | | | | | | | |
| 5 | Missing values: drop, default, or keep and flag | | | | | | | |
| 6 | Each join: type, key, validation | | | | | | | |
| 7 | The method (tree / ladder / bridge / shuffle / comparison) | | | | | | | |
| 8 | The segmentation (city, channel, type) | | | | | | | |
| 9 | The chart that carries the claim | | | | | | | |
| 10 | The one sentence | | | | | | | |
| 1 | Which table should be used for source of truth for tests | 1.Bookings legacy,count rows , 2.Bookings legacy, count distinct booking_id. | Bookings legacy is the source of truth for booking_id, slot_at and patient_id | It holds the booking identity and slot time and grain is booking-test (2.35 rows per booking_id), so count distinct bookings  | nothing currently | Profiled: 19,602 rows for 8,344 distinct booking_id in the largest file; 46 ids fail the pattern after strip. | Rohit | 2026-10-24 |
| 11 | SQL engine for notebook 04 (SQLite only) | (a) PostgreSQL via `KALPA_PG`. (b) SQLite file at `data/clean/kalpa.sqlite`, rebuilt on every run. | (b) SQLite | No server to install or share, runs in a fresh Codespace, and `03_profile.sql` and `04_transformations.sql` both run on it. | A PostgreSQL instance available to the whole group, or a need to show the index and EXPLAIN ANALYZE timing. | Loaded bookings 563,380, patients 303,153, invoices 470,776, payments 473,507, plan 36 rows. File is about 239 MB. `05_performance.sql` is skipped, so the index claim is untested. | Rohit | 2026-10-24 |
| 12 | Running the PostgreSQL-written SQL on SQLite | (a) Maintain a separate SQLite copy of each file. (b) Keep one file and substitute in `run_sql`: `date_trunc('month', ` to `strftime('%Y-%m', `, drop `::date` and `::numeric`, `EXTRACT(YEAR FROM ` to `strftime('%Y', `. | (b) | One source of SQL for finance to re-run, no drift between two copies. | SQL that uses syntax a string replace cannot translate. | Sections 1 to 4 of `04_transformations.sql` printed results. Substitution is textual, so a new PostgreSQL-only construct could break silently. | Rohit | 2026-10-24 |
| 13 | Performance section on SQLite | (a) Time the monthly rollup in SQLite with and without an index. (b) Skip `05_performance.sql` on SQLite and record that it was not run. | (b) | SQLite's planner and `EXPLAIN` output differ from PostgreSQL, so numbers from it would not support a PostgreSQL claim. | Being asked to defend the index on SQLite specifically. | Cell prints "Skipped on SQLite". No timing or EXPLAIN evidence exists. | Rohit | 2026-10-24 |
| 14 | Loading clean tables into the database | (a) `pandas.to_sql` from the clean CSVs. (b) Run `01_schema.sql` and `02_load.sql` (typed schema, bulk load). | (a) | One call per table, with dates parsed on read. | Needing declared types, keys and constraints in the database. | Worked. `to_sql` creates untyped tables with no keys, so the grain is checked by query (`max_rows_per_booking` = 1), not by a constraint. | Rohit | 2026-10-24 |

## Parts we never had to choose about

<List any part where only one approach was possible, and say why. The panel will ask whether that was true.>
