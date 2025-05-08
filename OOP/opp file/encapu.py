class secretstash:
    def __init__(self):
        self.__chocolate=10 # private attribute

    def get_chocolate(self):
        if self.__chocolate>0:
            self.__chocolate-=1
            print("one chocolate taken")
        else:
            print("no more chocolate left")
stash =secretstash()
stash.take_chocolate()