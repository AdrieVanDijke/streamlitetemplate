from a3d.controlers.c_base import BaseControler


class DevelopingControler(BaseControler):
    def __init__(self):
        super().__init__()
        print("Initialising DevelopingControler")

    # Cache legen geheugen wissen ===============
    def reset(self):
        print("Resetting DevelopingControler")

    # MAIN =====================================
    def run(self):
        print("Geactiveerd DevelopingControler")

    # WORKERS ==================================

    # DATA =====================================