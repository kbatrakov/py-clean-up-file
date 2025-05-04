import os
from typing import TextIO
from typing import Optional, Type
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.filename)
        return self.file

    def __exit__(self, exc_type: Optional[Type[BaseException]] ,
                 exc_val: Optional[BaseException], exc_tb:
                 Optional[TracebackType]) -> None:
        self.file.close()
        os.remove(self.filename)
