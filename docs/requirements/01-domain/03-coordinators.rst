02-Repositories
---------------

..
    .. estimark:
       :classifiers: M, DOMAIN


Story
^^^^^

| As a developer
| I want to define application coordinators
| So that I can manage the transactional interactions

Validation Criteria
^^^^^^^^^^^^^^^^^^^

| Given the application repositories have been defined,
| When I access the application coordinators package
| Then it will be possible to orchestrate the core system functionalities

| Given the coordinators package has been defined
| When I instantiate the calibration coordinator
| Then I will be able to create classifiers and assign their efforts.

| Given the coordinators package has been defined
| When I instantiate the assignation coordinator
| Then I will be able to define then executors of the project

| Given the coordinators package has been defined
| When I instantiate the planning coordinator 
| Then I will be able to create tasks with their dependencies
