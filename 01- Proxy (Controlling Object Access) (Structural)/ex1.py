class Player:
    def __init__(self):
        self.hasContract = True

    def occupied(self):
        self.hasContract = True
        print(type(self).__name__, "is working with a team.")

    def available(self):
        self.hasContract = False
        print(type(self).__name__, "is available for transfer.")

    def get_status(self):
        return self.hasContract


class Agent:
    def __init__(self):
        self.player = None

    def work(self):
        self.player = Player()
        if self.player.get_status():
            self.player.occupied()
        else:
            self.player.available()


if __name__ == '__main__':
    a = Agent()
    a.work()
