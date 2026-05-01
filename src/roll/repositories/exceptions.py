class QueryFailedPrepareError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class QueryFailedExecError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
