from taipy.gui import Gui, Icon, navigate
import taipy.gui.builder as tgb
from pages.sales_page import sales_page
from pages.sales_vorarlberg_page import sales_vorarlberg_page
from pages.max_page import max_page

def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)


with tgb.Page() as root_page:
    tgb.menu(
        label="Menu", Icon="images/icon_data.svg",
        lov=[
            ("sales", Icon("images/map.png", "Sales")),
            ("page_vorarlberg", Icon("images/map.png", "Vorarlberg Sales")),
            ("max", Icon("images/person.png", "Max")),
        ],
        on_action=menu_option_selected,
    )




pages = {"/": root_page, "sales": sales_page, "page_vorarlberg": sales_vorarlberg_page, "max": max_page}


Gui(pages=pages).run(title="Sales", dark_mode=False)
