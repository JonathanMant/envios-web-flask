from typing import Optional


class Bulk:
    def __init__(
            self,
            bulk_id: int,
            idbulk: int,
            status: int,
            name: str,
            retries: Optional[int] = None,
    ):
        self.bulk_id: int = bulk_id
        self.idbulk = idbulk
        self.status: int = status
        self.name: str = name
        self.retries: int = retries

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Bulk):
            return self.bulk_id == obj.bulk_id
        return False

