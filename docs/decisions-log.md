# Decisions log · cleaning and reconciliation · Brief A · Group 4

Every act of cleaning is a decision with a reason and an effect. Input equals clean plus rejected, every time. The headline number is recomputed after every decision so the bridge from raw to final is visible.

## Reconciliation

| Step | Table | Rows in | Rows kept | Rows rejected | In = kept + rejected? | Headline number after this step | Owner | Date |
|---|---|---|---|---|---|---|---|---|

## Decisions

| # | Table | What we found | Decision (drop / default / keep and flag / map / split) | Reason | Rows affected | Effect on the headline | Reversible? | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | bookings | Nova adds a new booking on reschedule and marks the old one `rescheduled`. Legacy edits the slot in place. | Drop the superseded old record | One visit = one booking. Makes nova and legacy comparable. | 1499 | 564,879 -> 563,380 bookings (-0.27%); 1,307,260 -> 1,303,719 tests | yes | Rohit |
| 2 | collections | Same booking, status and time scanned twice | Drop exact duplicates, keep first | A double scan is one collection | 2894 | none on bookings; collections 552,492 -> 549,598 | yes | Rohit |
| 3 | bookings | 18,269 bookings have no collection row | Keep, set status `cancelled_or_missing` | The app does not record cancels, so cancelled and missing cannot be told apart. Ask the data team. | 18269 | none (rows kept), but the headline still includes them | yes | Rohit |
| 4 | bookings | 936 collections are stamped over 1 day before the slot (clock skew?) | Keep the row, blank `collected_at`, set `flag_clock_skew` | The time is wrong but the booking is real | 936 | none | yes | Rohit |
| 5 | patients | 6,064 of 309,217 rows share phone+name+dob with an earlier row; 1,492 have placeholder dob 1900-01-01 | Merge into one person (keep first), re-key bookings to the person | Growth analysis only. A wrong merge slightly skews frequency. No reports go to patients. | 6064 | 309,217 -> 303,153 patients (-2.0%); bookings unchanged | yes | Rohit |
| 6 | invoices, payments | 1,925 invoices have 2+ captured payments, 21,820 have none, 4,588 payments have no invoice | Keep all, no rule yet | Needs finance input before dropping anything | 0 | none yet. Rs 737,020,069 invoiced | yes | Rohit |
| 1 | bookings_legacy | header line repeated mid-file | drop | an append artefact, not data | 0 | none (not rows) | yes | <name> |
| 1 | bookings_legacy | 21 repeated header lines inside appended exports | drop | They are repeated column headings, not booking records. | 21 header lines | No booking records removed; no direct effect on the headline. | yes | chaitanya |
| 2 | bookings_all | 3,107 booking records failed model validation; 564,879 passed | split | Keep failures in the rejects file with their validation reasons; only accepted bookings enter the validated booking table. | 3,107 rejected | The final effect on the Brief A metric must be measured after the cleaning and reconciliation decisions. | yes | chaitanya |
| 3 | bookings_all | 1,500 accepted Nova records have rescheduled_from populated | keep and flag | Preserve the reschedule information for the reschedule decision in notebook 03. | 1,500 flagged | Not decided here; notebook 03 will determine how reschedules affect the count. | yes | chaitanya |
| 4 | bookings_all | The city label Bangalore was mapped to Bengaluru | map | Use one consistent city label for grouping and reporting. | Bangalore entries; count not recorded | No change to total bookings; city-level grouping may change. | yes | chaitanya |

## Joins

| # | Left table (rows) | Right table (rows) | Key | Type | Rows after | Keys matched more than once | Explanation of the change in count | Owner |
|---|---|---|---|---|---|---|---|---|

## Cold runs

| Date | Who ran it | Fresh Codespace? | Runtime | Headline number | Same as last run? | If not, why |
|---|---|---|---|---|---|---|
| | | | | | | |
