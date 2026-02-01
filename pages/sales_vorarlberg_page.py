TOP_N_MIN = 5
TOP_N_MAX = 10
top_n = TOP_N_MIN

def get_top_city_sales(df, n):
    return (
        df.groupby("City")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
from taipy.gui import navigate
import taipy.gui.builder as tgb
from maps.vorarlberg_map import generate_vorarlberg_map
import pandas as pd

data = pd.read_csv("data/data_vorarlberg.csv")

def change_category(state):
    if state.selected_category == "All":
        state.subcategories = ["All"] + sorted(list(data["Sub-Category"].unique()))
        state.selected_subcategory = "All"
    else:
        state.subcategories = ["All"] + sorted(list(data[data["Category"] == state.selected_category]["Sub-Category"].unique()))
        state.selected_subcategory = "All"
    apply_changes(state)

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
    if state.selected_category != "All":
        state.data = state.data[state.data["Category"] == state.selected_category]
    if state.selected_subcategory != "All":
        state.data = state.data[state.data["Sub-Category"] == state.selected_subcategory]
    update_chart_and_map(state)

def update_top_n(state):
    update_chart_and_map(state)


def update_chart_and_map(state):
    state.chart_data = get_top_city_sales(state.data, state.top_n)
    state.layout = {
        "yaxis": {"title": "Revenue (EUR)"},
        "title": f"Sales by City for {state.selected_category} - {state.selected_subcategory}",
    }
    state.map_fig = generate_vorarlberg_map(state.chart_data)


categories = ["All"] + list(data["Category"].unique())
selected_category = "All"
subcategories = ["All"] + sorted(list(data["Sub-Category"].unique()))
selected_subcategory = "All"

start_date = pd.to_datetime(data["Order Date"], format="%d/%m/%Y").min()
end_date = pd.to_datetime(data["Order Date"], format="%d/%m/%Y").max()

top_n = TOP_N_MIN
chart_data = get_top_city_sales(data, top_n)

layout = {"yaxis": {"title": "Revenue (EUR)"}, "title": "Sales by City"}
map_fig = generate_vorarlberg_map(chart_data)

with tgb.Page() as sales_vorarlberg_page:
    with tgb.part(class_name="container"):
        tgb.text("# Sales by **City** (Vorarlberg)", mode="md")
        with tgb.part(class_name="card"):
            with tgb.layout(columns="1 2 1"):
                with tgb.part():
                    tgb.text("Filter **From**", mode="md")
                    tgb.date("{start_date}", format="dd-MM-yyyy", on_change=apply_changes)
                    tgb.text("**To**", mode="md")
                    tgb.date("{end_date}", format="dd-MM-yyyy", on_change=apply_changes)
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
                        on_change=apply_changes,
                        dropdown=True,
                        disabled="{selected_category} == 'All'",
                    )
                with tgb.part(class_name="text-center"):
                    tgb.text("Show top {top_n} cities:")
                    tgb.slider(
                        value="{top_n}",
                        min=TOP_N_MIN,
                        max=TOP_N_MAX,
                        step=1,
                        on_change=update_top_n,
                        show_value=True,
                    )
        tgb.html("br")
        with tgb.layout(columns="2 3"):
            tgb.chart(
                data="{chart_data}",
                x="City",
                y="Sales",
                type="bar",
                layout="{layout}",
            )
            tgb.chart(figure="{map_fig}")
        tgb.html("br")
        tgb.table(data="{data}")
