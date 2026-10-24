# Decisions log · cleaning and reconciliation · Brief A · Group 4

Every act of cleaning is a decision with a reason and an effect. Input equals clean plus rejected, every time. The headline number is recomputed after every decision so the bridge from raw to final is visible.

## Reconciliation

| Step | Table | Rows in | Rows kept | Rows rejected | In = kept + rejected? | Headline number after this step | Owner | Date |
|---|---|---|---|---|---|---|---|---|
| 0 | raw as received | | | | | | | |
| 1 | | | | | | | | |

## Decisions

| # | Table | What we found | Decision (drop / default / keep and flag / map / split) | Reason | Rows affected | Effect on the headline | Reversible? | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 1 | bookings_legacy | header line repeated mid-file | drop | an append artefact, not data | 0 | none (not rows) | yes | <name> |
| 1 | bookings_legacy | 21 repeated header lines inside appended exports | drop | They are repeated column headings, not booking records. | 21 header lines | No booking records removed; no direct effect on the headline. | yes | chaitanya |
| 2 | bookings_all | 3,107 booking records failed model validation; 564,879 passed | split | Keep failures in the rejects file with their validation reasons; only accepted bookings enter the validated booking table. | 3,107 rejected | The final effect on the Brief A metric must be measured after the cleaning and reconciliation decisions. | yes | chaitanya |
| 3 | bookings_all | 1,500 accepted Nova records have rescheduled_from populated | keep and flag | Preserve the reschedule information for the reschedule decision in notebook 03. | 1,500 flagged | Not decided here; notebook 03 will determine how reschedules affect the count. | yes | chaitanya |
| 4 | bookings_all | The city label Bangalore was mapped to Bengaluru | map | Use one consistent city label for grouping and reporting. | Bangalore entries; count not recorded | No change to total bookings; city-level grouping may change. | yes | chaitanya |

## Joins

| # | Left table (rows) | Right table (rows) | Key | Type | Rows after | Keys matched more than once | Explanation of the change in count | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

## Cold runs

| Date | Who ran it | Fresh Codespace? | Runtime | Headline number | Same as last run? | If not, why |
|---|---|---|---|---|---|---|
| | | | | | | |
