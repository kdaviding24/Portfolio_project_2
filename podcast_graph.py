from podcast import Podcast


class Podcast_graph:
    def __init__(self):
        self.podcast_dict = {}
    
    def add_podcast(self, name, genre):
        podcast = Podcast(name, genre)
        for genre in podcast.genre:
            if genre not in self.podcast_dict:
                self.podcast_dict[genre] = [podcast]
            else:
                self.podcast_dict[genre].append(podcast)


    def grab_by_genre(self, genre):
        print("Recommended Podcasts: ")
        for podcast in self.podcast_dict[genre]:
            print(f"\n {podcast.name}")
    

podcast_menu = {'JRE': ['Information', 'Comedy', 'Entertainment'], 
            'Tim Dillon Show': ['Comedy', 'Information', 'Entertainment']}



spahdefy = Podcast_graph()
for podcast in podcast_menu:
    spahdefy.add_podcast(podcast, podcast_menu[podcast])

print(spahdefy.podcast_dict)
spahdefy.grab_by_genre('Entertainment')