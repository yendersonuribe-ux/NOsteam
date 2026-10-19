
from game import Game


class Cart:
    """Manage the games added to the shopping cart."""

    def __init__(self):
        self.games: list[Game] = []

    def add_game(self, game: Game) -> bool:
        """Add a game if it is not already in the cart."""
        if any(item.title == game.title for item in self.games):
            return False

        self.games.append(game)
        return True

    def remove_game(self, game: Game):
        """Remove a game from the cart."""
        self.games = [
            item for item in self.games
            if item.title != game.title
        ]

    def get_total(self) -> float:
        """Calculate the total price."""
        return sum(game.price for game in self.games)
