from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label

class ListViewExample(App):
    def set_paragraphs(self, paragraphs):
        self.paragraphs = paragraphs

    def compose(self) -> ComposeResult:
        list_view = ListView()
        for item in self.paragraphs:
            list_view.append(ListItem(Label(item)))
        yield list_view


def show(paragraphs):
    app = ListViewExample()
    app.set_paragraphs(paragraphs)
    app.run()
