from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label

class ListViewExample(App):
    CSS_PATH = "general.css"
    def set_items(self, items):
        self.items = items

    def compose(self) -> ComposeResult:
        list_view = ListView()
        for item in self.items:
            list_view.append(ListItem(Label(item)))
        yield list_view


def show(items):
    app = ListViewExample()
    app.set_items(items)
    app.run()
