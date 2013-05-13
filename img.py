class img:
    offset_x = 0
    offset_y = 0
    surface = None
    
    def __init__(self, offset_x, offset_y, surface):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.surface = surface