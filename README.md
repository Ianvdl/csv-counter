# csv-counter

A simple script to count the number of records in a given list of CSV files. This is useful for verification after database loads as it takes into account newlines inside quoted strings, something a command like `wc -l` does not do.

Example:

```
python3 csv-counter.py *.csv
```

Example output:

```
All counts exclude header row. One header row is assumed per file.

g_applicant_not_disambiguated.csv                 : 5,136,615
g_application.csv                                 : 8,257,883
g_assignee_disambiguated.csv                      : 7,596,786
g_assignee_not_disambiguated.csv                  : 7,596,786
g_attorney_disambiguated.csv                      : 9,283,885
g_attorney_not_disambiguated.csv                  : 9,383,336
g_botanic.csv                                     : 19,148
g_cpc_current.csv                                 : 48,473,812
g_cpc_title.csv                                   : 264,485
g_examiner_not_disambiguated.csv                  : 11,085,926
g_figures.csv                                     : 7,711,478
g_foreign_citation.csv                            : 35,757,764
g_foreign_priority.csv                            : 3,827,627
g_gov_interest.csv                                : 165,835
g_gov_interest_contracts.csv                      : 201,535
g_gov_interest_org.csv                            : 200,950
g_inventor_disambiguated.csv                      : 20,427,566
g_inventor_not_disambiguated.csv                  : 20,427,607
g_ipc_at_issue.csv                                : 20,730,648
g_location_disambiguated.csv                      : 81,837
g_location_not_disambiguated.csv                  : 33,168,375
g_other_reference.csv                             : 51,660,341
g_patent.csv                                      : 8,260,142
g_pct_data.csv                                    : 1,810,551
g_persistent_assignee.csv                         : 7,596,786
g_persistent_inventor.csv                         : 20,427,566
g_rel_app_text.csv                                : 2,240,992
g_us_application_citation.csv                     : 56,881,814
g_us_patent_citation.csv                          : 128,401,915
g_us_rel_doc.csv                                  : 13,211,907
g_us_term_of_grant.csv                            : 4,160,366
g_uspc_at_issue.csv                               : 14,139,741
g_wipo_technology.csv                             : 11,076,102

Done.
```
