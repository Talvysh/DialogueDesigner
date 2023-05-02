class Requirement():
    def __init__(self, id: str, val: any) -> None:
        pass


class Dialogue():
    def __init__(self) -> None:
        self.content = ""  # The text this dialogue outputs.
        self.connect_to: Dialogue
        self.hidden: bool
        self.requirements = []
    

    def add_req(self, req) -> None:
        self.requirements.append(req)


    def check_reqs(self) -> bool:
        return True


def example():
    dia = Dialogue()
    dia.add_req("the-id", True)