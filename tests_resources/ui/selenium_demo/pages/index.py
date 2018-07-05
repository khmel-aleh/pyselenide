from .drag_and_drop import SDDragAndDrop
from .hover import SDHover
from .key_press import SDKeyPress

class SeleniumDemo(
    SDDragAndDrop,
    SDHover,
    SDKeyPress
):
    pass
