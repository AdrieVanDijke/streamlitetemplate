from a3d.controlers.c_base import BaseControler


class HomeControler(BaseControler):
    def __init__(self):
        super().__init__()
        print("Initialising HomeControler")
  
     # Cache legen geheugen wissen ===============
    def reset(self):
        print("Resetting HomeControler")

    # MAIN =====================================
    def run(self):
        print("Geactiveerd HomeControler")
    # WORKERS ==================================

    # DATA =====================================
