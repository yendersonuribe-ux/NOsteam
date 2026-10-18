
import flet as ft

from game import Game


class GameStore:
    """Main class for the NOsteam game store."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.games = self.get_games()

        self.page.title = "NOsteam - PC Game Store"
        self.page.bgcolor = "#343A32"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        self.page.spacing = 0

        self.search_query = ""
        self.selected_genre = "All"
        # Navigation
        self.current_view = "store"
        self.selected_game = None

        # Shopping cart and user library
        self.cart = []
        self.library = []

   
    
    def get_games(self):
        """Return the game collection."""
        return [
            Game(
                "Boosborne",
                "Action",
                19.99,
                "Bienvenido a una ciudad donde todo quiere matarte. "
                "Sobrevive a tus pesadillas y recuerda: morir también "
                "es una forma de aprender.",
                "boosborne.png",
            ),
            Game(
                "Falos",
                "RPG",
                14.99,
                "El mundo acabó y nadie avisó. Explora el yermo, "
                "consigue chatarra y descubre que sobrevivir al "
                "apocalipsis es otro trabajo sin sueldo.",
                "falos.png",
            ),
            Game(
                "Melda",
                "Adventure",
                7.99,
                "Un reino necesita un héroe, una princesa necesita "
                "ayuda y tú necesitas recordar qué misión estabas "
                "haciendo después de distraerte durante tres horas.",
                "Melda.png",
            ),
            Game(
                "Walcra III: Silla helada",
                "Strategy",
                9.99,
                "Construye tu base, reúne recursos y dirige ejércitos. "
                "Todo va bien hasta que descubres que tu enemigo "
                "lleva diez minutos preparando una silla.",
                "walcra III silla helada.png",
            ),
        ]



    
    def refresh_catalog(self, e=None):
        """Refresh the game cards using the active filters."""
        filtered_games = self.filter_games()

        self.catalog_grid.controls = [
            self.build_game_card(game)
            for game in filtered_games
        ]

        self.catalog_grid.update()


    def build_header(self):
        """Create the top navigation bar."""
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.GAMEPAD,
                                color="#C4D9EB",
                                size=30,
                            ),
                            ft.Text(
                                "NOsteam",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#FFFFFF",
                            ),
                        ],
                        spacing=8,
                    ),
                    ft.Row(
                        controls=[
                            ft.TextButton("HOME"),
                            ft.TextButton("STORE"),
                            ft.TextButton("NEWS"),
                            ft.TextButton("COMMUNITY"),
                        ],
                        spacing=4,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor="#090B0D",
            padding=ft.Padding.symmetric(
                horizontal=24,
                vertical=12,
            ),
            border=ft.Border(
                bottom=ft.BorderSide(2, "#527DA0"),
            ),
        )

    def build_welcome(self):
        """Create the store welcome panel."""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "WELCOME TO NOsteam",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color="#8DBCE8",
                    ),
                    ft.Text(
                        "Your next adventure starts here.",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    ft.Text(
                        "Discover games and build your collection.",
                        color="#D1D8DF",
                    ),
                ],
                spacing=10,
            ),
            bgcolor="#41464B",
            padding=22,
            border=ft.Border.all(1, "#626970"),
            border_radius=5,
        )

   
    def build_game_card(self, game: Game):
        """Create a game card with its cover image."""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=game.cover_path,
                        width=float("inf"),
                        height=160,
                        fit=ft.BoxFit.COVER,
                        error_content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Icon(
                                        ft.Icons.VIDEOGAME_ASSET,
                                        size=42,
                                        color="#C4D9EB",
                                    ),
                                    ft.Text(
                                        "Cover coming soon",
                                        size=11,
                                        color="#CDD3D9",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor="#454C53",
                            alignment=ft.Alignment.CENTER,
                        ),
                    ),
                    ft.Text(
                        game.title,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    ft.Text(
                        game.genre,
                        size=12,
                        color="#A9C9E8",
                    ),
                    ft.Text(
                        game.description,
                        size=12,
                        color="#CDD3D9",
                    ),
                    ft.Text(
                        f"${game.price:.2f}",
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                ],
                spacing=8,
            ),
            bgcolor="#292D31",
            padding=10,
            border=ft.Border.all(1, "#50575E"),
            border_radius=4,
            width=280,
            on_click=lambda e: self.show_game_details(game)
        )


    def show_game_details(self, game: Game):
        """Show the selected game's details."""
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(game.title),
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=game.cover_path,
                        width=320,
                        height=180,
                        fit=ft.BoxFit.CONTAIN,
                    ),
                    ft.Text(f"Genre: {game.genre}"),
                    ft.Text(game.description),
                    ft.Text(
                        f"${game.price:.2f}",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                tight=True,
                scroll=ft.ScrollMode.AUTO,
            ),
            actions=[
                ft.TextButton(
                    "Close",
                    on_click=lambda e: self.page.pop_dialog(),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.show_dialog(dialog)

    
    def filter_games(self):
        """Return games matching the search and selected genre."""
        filtered_games = []

        for game in self.games:
            matches_search = (
                self.search_query.lower() in game.title.lower()
            )

            matches_genre = (
                self.selected_genre == "All"
                or game.genre == self.selected_genre
            )

            if matches_search and matches_genre:
                filtered_games.append(game)

        return filtered_games

        
    def on_search_change(self, e):
        """Update the search query when the user types."""
        self.search_query = e.control.value or ""
        self.refresh_catalog()


    def build_sidebar(self):
        """Create the persistent store sidebar."""
        genres = ["Action", "Adventure", "Strategy", "RPG"]

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "SEARCH",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                 
                        ft.TextField(
                            hint_text="Search games...",
                            text_size=13,
                            height=42,
                            content_padding=10,
                            border_color="#65717C",
                            bgcolor="#202428",
                            on_change=self.on_search_change,
                        ),

                    ft.Divider(color="#555C63"),
                    ft.Text(
                        "BROWSE BY GENRE",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    
                        ft.TextButton(
                            "All games",
                            on_click=lambda e: self.select_genre("All"),
                ),
                *[
                    ft.TextButton(
                        genre,
                        on_click=lambda e, selected=genre: self.select_genre(selected),
                    )
                    for genre in genres
                ],

                

                    ft.Divider(color="#555C63"),
                    ft.Text(
                        "SPECIAL OFFERS",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    ft.Text(
                        "Discover games and future discounts.",
                        size=12,
                        color="#CDD3D9",
                    ),
                    ft.Container(
                        content=ft.Text(
                            "COMING SOON",
                            size=11,
                            weight=ft.FontWeight.BOLD,
                            color="#FFFFFF",
                        ),
                        bgcolor="#58764B",
                        padding=10,
                        alignment=ft.Alignment.CENTER,
                        border_radius=3,
                    ),
                ],
                spacing=12,
                tight=True,
            ),
            bgcolor="#292D31",
            padding=14,
            width=245,
            border=ft.Border.all(1, "#50575E"),
            border_radius=4,
        )

    
    def select_genre(self, genre: str):
        """Select a genre and refresh the catalog."""
        self.selected_genre = genre
        self.refresh_catalog()


    
    def build(self):
        """Build the main store layout."""
        self.catalog_grid = ft.Row(
            controls=[
                self.build_game_card(game)
                for game in self.filter_games()
    ],
    spacing=12,
    vertical_alignment=ft.CrossAxisAlignment.START,
    wrap=True,
)

        main_content = ft.Column(
            controls=[
                self.build_welcome(),
                ft.Text(
                    "GAME CATALOG",
                    size=19,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF",
                ),
                self.catalog_grid,
            ],
            spacing=18,
            expand=True,
        )

        self.page.add(
            self.build_header(),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=main_content,
                            expand=True,
                        ),
                        self.build_sidebar(),
                    ],
                    spacing=18,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                padding=22,
                expand=True,
            ),
        )



def main(page: ft.Page):
    store = GameStore(page)
    store.build()


if __name__ == "__main__":
    ft.run(main)
