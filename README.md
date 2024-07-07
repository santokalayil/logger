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
## Logging Format Guide
```
%(name)s            Name of the logger (logging channel)
%(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                    WARNING, ERROR, CRITICAL)
%(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                    "WARNING", "ERROR", "CRITICAL")
%(pathname)s        Full pathname of the source file where the logging
                    call was issued (if available)
%(filename)s        Filename portion of pathname
%(module)s          Module (name portion of filename)
%(lineno)d          Source line number where the logging call was issued
                    (if available)
%(funcName)s        Function name
%(created)f         Time when the LogRecord was created (time.time()
                    return value)
%(asctime)s         Textual time when the LogRecord was created
%(msecs)d           Millisecond portion of the creation time
%(relativeCreated)d Time in milliseconds when the LogRecord was created,
                    relative to the time the logging module was loaded
                    (typically at application startup time)
%(thread)d          Thread ID (if available)
%(threadName)s      Thread name (if available)
%(process)d         Process ID (if available)
%(message)s         The result of record.getMessage(), computed just as
                    the record is emitted
```
