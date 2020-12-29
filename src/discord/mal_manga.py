import mal

class MangaQuery ():
    def __init__ (self, manga_name):
        self.user_request_manga_name = manga_name

    def search_manga_title (self):
        query = mal.MangaSearch (self.user_request_manga_name)
        query_manga_name = query.results[0].title

        return query_manga_name

    def serach_manga_url (self):
        query = mal.MangaSearch (self.user_request_manga_name)
        query_manga_url = query.results[0].url

        return query_manga_url

    def search_manga_synopsis (self):
        query = mal.MangaSearch (self.user_request_manga_name)
        query_manga_synopsis = query.results[0].synopsis

        return query_manga_synopsis

    def search_manga_score (self):
        query = mal.MangaSearch (self.user_request_manga_name)
        query_manga_score = query.results[0].score

        return query_manga_score

    def search_manga_image (self):
        query = mal.MangaSearch (self.user_request_manga_name)
        query_manga_image = query.results[0].image_url

        return query_manga_image

if __name__ == "__main__":
    manga = MangaQuery ("Bleach")

    print (manga.search_manga_image())
    print (manga.serach_manga_url())