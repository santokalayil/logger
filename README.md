# Simple Logger
This repository showcases how a logger class can be created for complicated python frameworks and platforms.
More and more customizations can be added. This is kept to simple so that everyone can understand and use it.
For each handlers, we can have seperate log levels, log formats. But class created in logger.py is set to use only common level and format. If you want to change it for your own usecase, please feel free to change it and use


- `main.py` contains example code how we can import and use the logger
- `logger.py` contains the logger class creation code
- `logger.yaml` contains the configuration file format

## Output in `app.log`
```log
2024-07-01 01:19:03,861 - __main__ - INFO - This is info
2024-07-01 01:19:03,862 - __main__ - WARNING - This is warning
2024-07-01 01:19:03,862 - __main__ - ERROR - This is error
2024-07-01 01:19:03,862 - __main__ - DEBUG - This is debugging message
```
## Logging Levels and Their Values
```python
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
```

