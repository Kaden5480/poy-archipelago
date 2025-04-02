class IDHandler:
    __id: int

    def __init__(self) -> None:
        self.__id = 1

    def new_id(self) -> int:
        ret = __id
        __id += 1

        return ret
