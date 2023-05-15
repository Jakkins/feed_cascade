from dataclasses import dataclass
from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label
from textual.containers import Container

@dataclass
class FeedMeItem:
    source: str
    text: str

class FeedMe(App):
    CSS_PATH = "general.css"
    def set_items(self, items):
        self.items = items

    def get_item(self, item: FeedMeItem):
        return ListItem(Container(
                Label("Horizontal"),
                Label(item.text),
                id="horizontal-layout",
        ))

    def compose(self) -> ComposeResult:
        list_view = ListView()
        for item in self.items:
            list_view.append(self.get_item(item))
        yield list_view
        yield Label("prova")


def show(items: list[FeedMeItem]):
    app = FeedMe()
    app.set_items(items)
    app.run()
