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
    state.chart_data = get_top_city_sales(state.data, state.top_n)
    state.layout = {
        "yaxis": {"title": "Revenue (EUR)"},
        "title": f"Sales by City for {state.selected_category} - {state.selected_subcategory}",
    }
    # Show only top N cities on the map as well
    state.map_fig = generate_vorarlberg_map(state.chart_data)

def update_top_n(state):
    state.chart_data = get_top_city_sales(state.data, state.top_n)
    state.layout = {
        "yaxis": {"title": "Revenue (EUR)"},
        "title": f"Sales by City for {state.selected_category} - {state.selected_subcategory}",
    }
    state.map_fig = generate_vorarlberg_map(state.chart_data)


categories = list(data["Category"].unique())
selected_category = categories[0]
selected_subcategory = list(data[data["Category"] == selected_category]["Sub-Category"].unique())[0]
subcategories = list(data[data["Category"] == selected_category]["Sub-Category"].unique())

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
                    tgb.date("{start_date}", format="dd-MM-yyyy")
                    tgb.text("**To**", mode="md")
                    tgb.date("{end_date}", format="dd-MM-yyyy")
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
                    tgb.text("Show top {top_n} cities:")
                    tgb.slider(
                        value="{top_n}",
                        min=TOP_N_MIN,
                        max=TOP_N_MAX,
                        step=1,
                        on_change=update_top_n,
                        show_value=True,
                    )
                    tgb.button(
                        "Apply",
                        class_name="plain apply_button_slider",
                        on_action=apply_changes,
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
