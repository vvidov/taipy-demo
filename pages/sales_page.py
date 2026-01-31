from taipy.gui import navigate
import taipy.gui.builder as tgb
from maps.us_map import generate_map
import pandas as pd

data = pd.read_csv("data/data.csv")
data = pd.read_csv("data/data.csv")
def change_category(state):
    state.subcategories = list(
        data[data["Category"] == state.selected_category]["Sub-Category"].unique()
    )
    state.selected_subcategory = state.subcategories[0]


def apply_changes(state):
    state.data = data[
        (
            pd.to_datetime(data["Order Date"], format="%d/%m/%Y")
            >= pd.to_datetime(state.start_date)
        )
        & (
            pd.to_datetime(data["Order Date"], format="%d/%m/%Y")
            <= pd.to_datetime(state.end_date)
        )
    ]
    state.data = state.data[state.data["Category"] == state.selected_category]
    state.data = state.data[state.data["Sub-Category"] == state.selected_subcategory]
    state.chart_data = (
        state.data.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    state.layout = {
        "yaxis": {"title": "Revenue (USD)"},
        "title": f"Sales by State for {state.selected_category} - {state.selected_subcategory}",
    }
    state.map_fig = generate_map(state.data)

categories = list(data["Category"].unique())
selected_category = "Furniture"
selected_subcategory = "Bookcases"
subcategories = list(
    data[data["Category"] == selected_category]["Sub-Category"].unique()
)

start_date = "2015-01-01"
end_date = "2018-12-31"

chart_data = (
    data.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

layout = {"yaxis": {"title": "Revenue (USD)"}, "title": "Sales by State"}
map_fig = generate_map(data)

with tgb.Page() as sales_page:
    with tgb.part(class_name="container"):
        tgb.text("# Sales by **State**", mode="md")
        with tgb.part(class_name="card"):
            with tgb.layout(columns="1 2 1"):
                with tgb.part():
                    tgb.text("Filter **From**", mode="md")
                    tgb.date("{start_date}")
                    tgb.text("**To**", mode="md")
                    tgb.date("{end_date}")
                with tgb.part():
                    tgb.text("Filter Product **Category**", mode="md")
                    tgb.selector(
                        value="{selected_category}",
                        lov=categories,
                        on_change=change_category,
                        dropdown=True,
                    )
                    tgb.text("Filter Product **Subcategory**", mode="md")
                    tgb.selector(
                        value="{selected_subcategory}",
                        lov="{subcategories}",
                        dropdown=True,
                    )
                with tgb.part(class_name="text-center"):
                    tgb.button(
                        "Apply",
                        class_name="plain apply_button",
                        on_action=apply_changes,
                    )
        tgb.html("br")
        with tgb.layout(columns="2 3"):
            tgb.chart(
                data="{chart_data}",
                x="State",
                y="Sales",
                type="bar",
                layout="{layout}",
            )
            tgb.chart(figure="{map_fig}")
        tgb.html("br")
        tgb.table(data="{data}")
