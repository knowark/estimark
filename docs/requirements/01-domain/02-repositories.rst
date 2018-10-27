02-Repositories
---------------

..
    .. estimark:
       :classifiers: M, DOMAIN


Story
^^^^^

| As a developer
| I want to define model repositories
| So that I can abstract away data access

Validation Criteria
^^^^^^^^^^^^^^^^^^^

| Given the application models have been defined
| When I import any of their repositories
| They will have the search, get, add and delete methods defined

| Given the abstract repositories have been defined
| When I instantiate their in memory implementations
| They will have abstract methods implemented.
