class Podcast:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
    

    def get_name(self):
        print(self.name)

    
    def get_genre(self):
        if len(self.genre) <= 1:
            print(self.genre)
        else:
            print(f'The genre(s) of this podcast is {self.genre.join(", ")}')
