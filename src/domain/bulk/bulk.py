from typing import Optional


class Bulk:
    def __init__(
            self,
            idbulk: int,
            status: int,
            name: str,
            id: Optional[int] = None,
            retries: Optional[int] = None,
    ):
        self.id: int = id
        self.idbulk = idbulk
        self.status: int = status
        self.name: str = name
        self.retries: int = retries

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Bulk):
            return self.id == obj.id
        return False

