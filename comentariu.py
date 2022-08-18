# smoke testing - primul test realizat după primirea unui build, - care verifică funcționalitățile generale; - dacă
#                 este realizat cu succes: e stabil - se trec la urm. tipuri de testări.
#                 if it fails - nu e stabil => reject the build
#
# sanity testing - făcut pe un test deja stabil (realizat după smoke testing)
#                  - are în vedere realizarea unor schimbări minore sau a fixa niște bug-uri,
#                  - adică testează funcționalitățile programului în profunzime
#                  - subset of regression testing
#                  - if it fails - reject the build
#
# regression testing - este realizat după ce, au fost adăugate părți de cod noi într-un program
#                    - pt a verifica dacă au apărut probleme noi sau efecte secundare ale codului nou la program
#                    - poate fi o combinație de smoke testing și sanity testing la un loc
#                    - de obicei este necesară când:
#                               au fost adăugate feature-uri noi SAU
#                               când au fost îmbunătățite feature-uri deja existente SAU
#                               după rezolvarea unor bug-uri
#                    - important info:
#                       If a huge list of regression tests are required to be executed, we can prioritize the important
#                       tests and execute them based on Risk-based approach. Instead of re-executing the entire test
#                       suite, it’s better to select the test cases for regression testing from the day one of
#                       the projects.
#                       Using the following parameters, we can select the tests:
#                               > Test cases which fail often
#                               > Test cases related to functionalities which are more visible and used
#                                 in the application
#                               > Test cases related to core functionalities of the application
#                               > Test cases of the functionalities which have been changed recently in the application
#
# equivalence partitioning/ equivalence class partitioning:
#               - type of black box testing technique
#               - It divides the input data of software into different equivalence data classes
#                 (un fel de Divide et Impera din C++)
#               - pentru fiecare subproblemă se aplică boundary testing (la limitele intervalelor)
#
# Boundary Value Analysis (BVA) - in Boundary Value Analysis, you test boundaries between equivalence partitions
#                                 (deci boundary testing...?!)
#
# boundary testing - the process of testing the extreme ends or between the input variables.
#                  - kinda like work smart, not harder
#                  - the basic idea is to select input var values at their:
#                           1. Minimum
#                           2. Just above the minimum
#                           3. A nominal value (ceva între min și max, la mijloc)
#                           4. Just below the maximum
#                           5. Maximum
#                  - se face după Equivalence Class Partitioning
#
# docstring = a multi-line comment between triple quotation mark (sau între 3 apostrofuri) placed in the first lines of
#             a function, method, class, or module
#           - hovering over the function when called will give as an explanation the docstring
