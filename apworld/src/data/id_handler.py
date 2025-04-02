class IDHandler:
    __id: int

    def __init__(self) -> None:
        """
        Initializes an IDHandler object.
        """

        self.__id = 1

    def new_id(self) -> int:
        """
        Gets a new ID to assign to data.

        :returns: The new ID
        """

        ret = self.__id
        self.__id += 1

        return ret
