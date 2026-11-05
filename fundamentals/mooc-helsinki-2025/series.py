class Series:
    """A TV series with seasons, genres and user ratings."""

    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        """Add a rating between 0 and 5."""
        if 0 <= rating <= 5:
            self.ratings.append(rating)

    def average_rating(self):
        """Return the average rating, or 0 if there are no ratings."""
        if len(self.ratings) == 0:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        genre_string = ', '.join(self.genres)

        if len(self.ratings) == 0:
            rating_info = 'no ratings'
        else:
            rating_info = f'{len(self.ratings)} ratings, average {self.average_rating():.1f} points'

        return (
            f'{self.title} ({self.seasons} seasons)\n'
            f'genres: {genre_string}\n'
            f'{rating_info}'
        )


def minimum_grade(rating: float, series_list: list):
    """Return the series whose average rating is at least the given value."""
    return [
        series for series in series_list
        if series.ratings and series.average_rating() >= rating
    ]


def includes_genre(genre: str, series_list: list):
    """Return the series that include the given genre."""
    return [series for series in series_list if genre in series.genres]
