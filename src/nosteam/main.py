
import flet as ft

from game import Game
from cart import Cart

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
        self.cart = Cart()
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

        self.cart_count = ft.Text(
            str(len(self.cart.games)),
            color="#FFFFFF",
            weight=ft.FontWeight.BOLD,
        )

        self.cart_button = ft.TextButton(
            "CART",
            on_click=lambda e: self.show_cart(),
        )

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
                            ft.TextButton(
                                "STORE",
                                on_click=lambda e: self.show_store(),
                            ),
                            ft.TextButton(
                                "NEWS",
                                on_click=lambda e: self.show_news(),
                            ),
                            ft.TextButton(
                                "COMMUNITY",
                                on_click=lambda e: self.show_community(),
                            ),
                            ft.Row(
                                controls=[
                                    self.cart_button,
                                    self.cart_count,
                                ],
                                spacing=4,
                            ),
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
        """Display a dedicated page for the selected game."""
        self.current_view = "details"
        self.selected_game = game

        self.view_container.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        "← Back to Store",
                        on_click=lambda e: self.show_store(),
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src=game.cover_path,
                                    width=360,
                                    height=250,
                                    fit=ft.BoxFit.CONTAIN,
                                ),
                                bgcolor="#202428",
                                padding=12,
                                border_radius=6,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        game.title,
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                        color="#FFFFFF",
                                    ),
                                    ft.Text(
                                        game.genre,
                                        size=15,
                                        color="#A9C9E8",
                                    ),
                                    ft.Divider(color="#50575E"),
                                    ft.Text(
                                        game.description,
                                        size=15,
                                        color="#CDD3D9",
                                    ),
                                    ft.Text(
                                        f"${game.price:.2f}",
                                        size=26,
                                        weight=ft.FontWeight.BOLD,
                                        color="#FFFFFF",
                                    ),
                                    ft.Button(
                                         "Add to Cart",
                                         icon=ft.Icons.SHOPPING_CART,
                                         on_click=lambda e: self.add_to_cart(game),
                                        )
                                ],
                                spacing=16,
                                expand=True,
                            ),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        spacing=24,
                    ),
                ],
                spacing=24,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=24,
            expand=True,
        )

        self.view_container.update()


    
    def add_to_cart(self, game: Game):
        added = self.cart.add_game(game)

        print("Juego añadido:", added)
        print("Juegos en el carrito:", len(self.cart.games))

        if not added:
            message = "Este juego ya está en el carrito."
        else:
            message = f"{game.title} se añadió al carrito."

        self.page.overlay.append(
            ft.SnackBar(content=ft.Text(message))
        )
        self.page.overlay[-1].open = True

        self.update_cart_button()
        self.page.update()

    
    def update_cart_button(self):
        count = len(self.cart.games)

        self.cart_count.value = str(count)

        print("Contador actualizado:", count)

        self.page.update()



    def remove_from_cart(self, game: Game):
        self.cart.remove_game(game)
        self.update_cart_button()
        print("Total guardado:", len(self.cart.games))
        print("Texto del contador:", self.cart_count.value)
        self.show_cart()

    def get_cart_total(self):
        return self.cart.get_total()

    
  
    def update_cart_button(self):
        count = len(self.cart.games)

        self.cart_count.value = str(count)
        self.cart_button.text = f"CART"

        print("Contador actualizado:", count)

        self.page.update()



    def show_cart(self):
        """Display the shopping cart."""
        self.current_view = "cart"

        if not self.cart.games:
            cart_content = ft.Column(
                controls=[
                    ft.Text(
                        "Your cart is empty",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    ft.Text(
                        "Explore the store and add some games.",
                        color="#CDD3D9",
                    ),
                ],
                spacing=12,
            )
        else:
            cart_content = ft.Column(
                controls=[
                    ft.Text(
                        "YOUR SHOPPING CART",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    *[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    game.title,
                                    color="#FFFFFF",
                                    expand=True,
                                ),
                                ft.Text(
                                    f"${game.price:.2f}",
                                    color="#FFFFFF",
                                ),
                                ft.TextButton(
                                    "Remove",
                                    on_click=lambda e, selected=game:
                                        self.remove_from_cart(selected),
                                ),
                            ],
                        )
                        for game in self.cart.games
                    ],
                    ft.Divider(color="#50575E"),
                    ft.Text(
                        f"Total: ${self.get_cart_total():.2f}",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                ],
                spacing=14,
            )

        self.view_container.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        "← Back to Store",
                        on_click=lambda e: self.show_store(),
                    ),
                    cart_content,
                ],
                spacing=24,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=24,
            expand=True,
        )
        self.view_container.update()




            
    def show_news(self):
        self.current_view = "news"

        self.view_container.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        "← Back to Store",
                        on_click=lambda e: self.show_store(),
                    ),
                    ft.Text(
                        "LATEST NEWS",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Welcome to NOsteam",
                                    size=19,
                                    weight=ft.FontWeight.BOLD,
                                    color="#FFFFFF",
                                ),
                                ft.Text(
                                    "Discover our catalog of games. "
                                    "More news and updates are coming soon.",
                                    color="#CDD3D9",
                                ),
                            ],
                            spacing=10,
                        ),
                        bgcolor="#292D31",
                        padding=20,
                        border=ft.Border.all(1, "#50575E"),
                        border_radius=4,
                    ),
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=24,
            expand=True,
        )
        self.view_container.update()




    def show_community(self):
        self.current_view = "community"

        self.view_container.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        "← Back to Store",
                        on_click=lambda e: self.show_store(),
                    ),
                    ft.Text(
                        "NOsteam COMMUNITY",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Welcome, player!",
                                    size=19,
                                    weight=ft.FontWeight.BOLD,
                                    color="#FFFFFF",
                                ),
                                ft.Text(
                                    "This is the community space for NOsteam. "
                                    "Community features will be added in the future.",
                                    color="#CDD3D9",
                                ),
                            ],
                            spacing=10,
                        ),
                        bgcolor="#292D31",
                        padding=20,
                        border=ft.Border.all(1, "#50575E"),
                        border_radius=4,
                    ),
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=24,
            expand=True,
        )
        self.view_container.update()



    
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


    
    
    def show_store(self):
        """Display the main store page."""
        self.current_view = "store"

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
            scroll=ft.ScrollMode.AUTO,
        )

        self.view_container.content = ft.Container(
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
        )

        self.view_container.update()


  
    def build(self):
        """Build the application and its navigation area."""
        self.view_container = ft.Container(expand=True)

        self.page.add(
            self.build_header(),
            self.view_container,
        )

        self.show_store()


def main(page: ft.Page):
    print("Archivo ejecutado:", __file__)
    print("¿Existe build?:", hasattr(GameStore, "build"))
    print("Métodos disponibles:", [
        name for name in GameStore.__dict__
        if not name.startswith("__")
    ])

    store = GameStore(page)
    store.build()


if __name__ == "__main__":
    ft.run(main)
