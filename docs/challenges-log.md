# Challenges log · Brief <LETTER> · Group <N>

What broke or surprised us, what we tried, what we changed and why. Entries are dated and written as they happen. A log written on the last evening answers no interview question, and the commit history shows which kind this is.

| # | Phase | What broke or surprised us | What we tried first | What we changed, and why | What we would do differently next time | Who | Date |
|---|---|---|---|---|---|---|---|
| 0 | *Profile and clean* | *Our first join of invoices to payments returned almost no matches.* | *Printed ten ids from each file side by side.* | *Wrote a mapping rule from invoice id to payment reference; kept unmappable rows in a separate list.* | *Profile id formats before writing any join.* | *example* | *example* |
| 1 | | | | | | | |
| 2 | SQL (SQLite) | `05_performance.sql` cannot run on SQLite: it uses `CREATE INDEX`, `ANALYZE` and `EXPLAIN ANALYZE` for PostgreSQL. | Considered running it anyway. | `run_sql` skips those statements on SQLite and the notebook prints "Skipped on SQLite". We record that no index or timing evidence exists. | Agree the database with the group before the SQL notebook, or set up one shared PostgreSQL. | Rohit | 2026-10-24 |
| 3 | SQL (SQLite) | The SQL files are written for PostgreSQL (`date_trunc`, `::date`, `::numeric`, `EXTRACT`) and SQLite rejects them. | Read the error from each query. | Added textual substitutions in `run_sql` so one set of files serves both engines. | Test each new query on SQLite as it is written. | Rohit | 2026-10-24 |
| 4 | SQL (SQLite) | `run_sql` turns a failing query into a one-row `error` table instead of stopping, so a failure looks like an output. | Noticed while reading the printed sections. | Check every printed section for an `error` column before trusting the notebook. | Make the notebook fail loudly on any error. | Rohit | 2026-10-24 |
| 5 | SQL (SQLite) | `kalpa.sqlite` is about 239 MB and the notebook deletes and rebuilds it on every run. | Saw it as untracked in git status. | Treat it as a build artefact: do not commit it, rebuild from the clean CSVs. | Add it to `.gitignore`. | Rohit | 2026-10-24 |
|  | Methods (step 1) | Growth reproduced as +5.03% against Dr Menon's 5 percent. Raw rows give +5.78%, and the CONFIG `between()` filter leaves out 30 June in both halves. | Rebuilt the count after each cleaning rule (raw, minus rejects, minus superseded originals) and with whole days. | Count clean `n_tests` per half with the CONFIG filter: 431,261 and 452,933. The identity rule moves the rate -0.81 pts, the rejects +0.06 pts. With whole days: 433,611 and 455,383 (+5.02%). | Filter timestamps with >= start and < day after end; between() on date strings drops the last day. | Rohit | 2026-10-24 |
|  | Methods: test volume vs the 5 percent | Rebuilt growth is +5.02% against the claimed 5%. The cell-2 filter gives +5.03%: between() on date strings ends at 00:00 on 30 June and leaves out 4,800 tests. | Rebuilt tests per half from the clean bookings with whole days, with the cell-2 filter, and before the identity rule (+5.84%). | Headline uses whole days (label_half): 433,611 and 455,383 tests, +5.02%. | Filter timestamps with >= first day and < the day after the last; never between() on date strings. | Rohit | 2026-10-24 |

## The entry we are proudest of

<One paragraph on the problem that taught the group the most. This is the story each of you tells in the viva.>
