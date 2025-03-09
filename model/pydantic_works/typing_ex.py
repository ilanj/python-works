from typing import List, Optional


class Student:
    def __init__(self):
        self.name: int = "ila"
        self.no: str = 36

    def get_name(self) -> int:
        return self.name


if __name__ == "__main__":
    run = Student()
    print(run.get_name())
