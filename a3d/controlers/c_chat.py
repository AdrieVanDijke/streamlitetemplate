from a3d.controlers.c_base import BaseControler


class ChatControler(BaseControler):
    def __init__(self):
        super().__init__()
        print("Initialising ChatControler")

    # Cache legen geheugen wissen ===============
    def reset(self):
        print("Resetting ChatControler")

    # MAIN =====================================
    def run(self):
        print("Geactiveerd ChatControler")

    # WORKERS ==================================

    # DATA =====================================