from Settings import Settings

s = Settings()


class Player:
    def __init__(self, player_number, color, right_key, left_key, up_key, down_key):
        self.num = player_number
        self.color = color
        self.pos = None
        self.drctn = None
        self.right = right_key
        self.left = left_key
        self.up = up_key
        self.down = down_key

    def setDirection(self, event):
        if event.key == self.right and self.drctn != "left":
            self.drctn = "right"

        if event.key == self.left and self.drctn != "right":
            self.drctn = "left"

        if event.key == self.up and self.drctn != "down":
            self.drctn = "up"

        if event.key == self.down and self.drctn != "up":
            self.drctn = "down"

    def movePlayer(self, grid):

        if self.drctn == "right":
            if self.pos[0] + 1 < s.blocks_x:
                if grid[self.pos[0] + 1, self.pos[1]] == 0:
                    self.pos = self.pos[0] + 1, self.pos[1]
                    return self.pos, self.num
                else:
                    return True
            else:
                return self.pos, self.num

        elif self.drctn == "left":
            if self.pos[0] - 1 >= 0:
                if grid[self.pos[0] - 1, self.pos[1]] == 0:
                    self.pos = self.pos[0] - 1, self.pos[1]
                    return self.pos, self.num
                else:
                    return True
            else:
                return self.pos, self.num

        elif self.drctn == "down":
            if self.pos[1] + 1 < s.blocks_y:
                if grid[self.pos[0], self.pos[1] + 1] == 0:
                    self.pos = self.pos[0], self.pos[1] + 1
                    return self.pos, self.num
                else:
                    return True
            return self.pos, self.num

        elif self.drctn == "up":
            if self.pos[1] - 1 >= 0:
                if grid[self.pos[0], self.pos[1] - 1] == 0:
                    self.pos = self.pos[0], self.pos[1] - 1
                    return self.pos, self.num
                else:
                    return True
            else:
                return self.pos, self.num

        else:
            return self.pos, self.num
