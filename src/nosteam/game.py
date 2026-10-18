
class Game:
    """Represent a video game in the store."""

    def __init__(
        self,
        title: str,
        genre: str,
        price: float,
        description: str,
        cover_path: str,
    ):
        self.title = title
        self.genre = genre
        self.price = price
        self.description = description
        self.cover_path = cover_path
