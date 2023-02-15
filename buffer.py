class Buffer:
    tc: str
    repeat: int
    work: int = 0
    amount: int = 0

    def __init__(self, tc: str, repeate: int) -> None:
        self.tc = tc
        self.repeat = repeate
