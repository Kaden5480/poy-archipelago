class IDHandler:
    _id: int

    def __init__(self) -> None:
        self._id = 1

    def new_id(self) -> int:
        ret = _id
        _id += 1

        return ret
