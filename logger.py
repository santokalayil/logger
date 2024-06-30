from typing import Dict, Any
from pathlib import Path
from logging import StreamHandler, Formatter, getLoggerClass,FileHandler
from logging.handlers import TimedRotatingFileHandler
import yaml

CONFIG_FILE = Path("logger.yaml")

__LoggerSuperClass = getLoggerClass()


class Logger(__LoggerSuperClass):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._level = self.config["LEVEL"]
        self._format = self.config["FORMAT"]
        self._file = self.config["FILE"]
        self._when = self.config["WHEN"]
        self._backupcount = self.config["BACKUP_COUNT"]
        self._formatter = Formatter(self._format)
        self.setLevel(self._level)
        self.set_console_handler()
        self.set_file_handler()
    
    @property 
    def config(self) -> Dict[str, Any]:
        return yaml.safe_load(Path(CONFIG_FILE).read_text())
    
    def set_console_handler(self) -> None:
        console_handler = StreamHandler()
        console_handler.setLevel(self._level)
        console_handler.setFormatter(self._formatter)
        self.addHandler(console_handler)
    
    def set_file_handler(self) -> None:
        # file_handler = FileHandler(self._file)
        file_handler = TimedRotatingFileHandler(self._file, when=self._when, backupCount=self._backupcount)
        file_handler.setLevel(self._level)
        file_handler.setFormatter(self._formatter)
        self.addHandler(file_handler)

if __name__ == "__main__":
    logger = Logger(__name__)
    logger.info("hi")


