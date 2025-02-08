from a3d.controlers.c_base import BaseControler


class HelpControler(BaseControler):
    def __init__(self):
        super().__init__()
        print("Initialising HelpControler")

    # Cache legen geheugen wissen ===============
    def reset(self):
        print("Resetting HelpControler")

    # MAIN =====================================
    def run(self):
        print("Geactiveerd HelpControler")

    # WORKERS ==================================

    # DATA =====================================