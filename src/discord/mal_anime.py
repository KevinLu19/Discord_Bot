import mal

class AnimeQuery ():
    def __init__ (self, anime_name):
        self.user_request_anime_name = anime_name

    def search_anime_title (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_user_anime = query.results[0].title

        return query_user_anime

    def search_anime_url (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_user_url = query.results[0].url

        return query_user_url

    def search_anime_synopsis (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_user_synopsis = query.results[0].synopsis

        return query_user_synopsis

    def search_anime_episodes (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_amount_episodes = query.results[0].episodes

        return query_amount_episodes

    def search_anime_score (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_score = query.results[0].score

        return query_score

    def search_anime_image_url (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_image = query.results[0].image_url

        return query_image

    def search_anime_type (self):
        query = mal.AnimeSearch (self.user_request_anime_name)
        query_anime_type = query.results[0].type

        return query_anime_type

if __name__ == "__main__":
    anime = AnimeQuery("Bleach")

    print (anime.search_anime_image_url())
    print (anime.search_anime_url())