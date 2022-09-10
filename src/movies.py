class Movie(object):
    """Base class: a movie starring Al Pacino"""
    title = None

    def get_title(self):
        if self.title is None:
            raise NotImplementedError()
        else:
            print(self.title)


class Gf(Movie):
    title = "The Godfather"


class Gf2(Movie):
    title = "The Godfather Part II"


class Gf3(Movie):
    title = "The Godfather Part III"


class Serpico(Movie):
    title = "Serpico"


class Scarface(Movie):
    title = "Scarface"


class Ggr(Movie):
    title = "Glengarry Glen Ross"


class Heat(Movie):
    title = "Heat"
