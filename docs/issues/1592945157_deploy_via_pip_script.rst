Deploy via pip script
=====================

Estimark should be installable via pip into virtual environments.
Using setup.py or poetry's scripts section in pyproject.toml, the programm
should be distributed as an executable through pip.

Validation Criteria
-------------------

- When installed through PIP, estimark should display its cli options behind
  the **estimark** command.
- Configuration options should be read by default from the current working
  directory in a config.json file.
