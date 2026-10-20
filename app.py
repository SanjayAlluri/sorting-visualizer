
import random
import time

import pandas as pd
import streamlit as st

from sorting_algorithms import ALGORITHMS, COMPLEXITIES


st.set_page_config(
    page_title="Sorting Visualizer",
    page_icon="📊",
    layout="wide",
)


def generate_array(size):
    """Generate a random array of positive integers."""
    return [random.randint(5, 100) for _ in range(size)]


def display_chart(placeholder, array):
    """Render the current array as a bar chart."""
    chart_data = pd.DataFrame({
        "Index": list(range(len(array))),
        "Value": array,
    })

    placeholder.bar_chart(
        chart_data,
        x="Index",
        y="Value",
        y_min=0,
        y_max=105,
    )


# ---------------- PAGE HEADER ----------------

st.title("📊 Sorting Algorithm Visualizer")

st.write(
    "Explore how different sorting algorithms organize "
    "an array, one step at a time."
)

st.divider()


# ---------------- SIDEBAR ----------------

st.sidebar.header("⚙️ Settings")

algorithm_name = st.sidebar.selectbox(
    "Choose an algorithm",
    list(ALGORITHMS.keys()),
)

array_size = st.sidebar.slider(
    "Array size",
    min_value=5,
    max_value=50,
    value=20,
)

animation_delay = st.sidebar.slider(
    "Animation delay (seconds)",
    min_value=0.01,
    max_value=0.30,
    value=0.05,
    step=0.01,
    help="A lower delay makes the animation faster.",
)

st.sidebar.caption(
    "Tip: Use a smaller array when learning how "
    "each algorithm works."
)


# ---------------- INITIALIZE ARRAY ----------------

if "array" not in st.session_state:
    st.session_state.array = generate_array(array_size)

# Generate a new array whenever the button is clicked.
if st.sidebar.button("🎲 Generate New Array", use_container_width=True):
    st.session_state.array = generate_array(array_size)

array = st.session_state.array.copy()


# ---------------- ALGORITHM INFORMATION ----------------

complexity = COMPLEXITIES[algorithm_name]

st.subheader(algorithm_name)

info_cols = st.columns(4)

info_cols[0].metric("Best Case", complexity["Best"])
info_cols[1].metric("Average Case", complexity["Average"])
info_cols[2].metric("Worst Case", complexity["Worst"])
info_cols[3].metric("Space Complexity", complexity["Space"])

st.caption(
    "The chart shows the values in the array. "
    "The horizontal axis represents the index, "
    "and the vertical axis represents the value."
)

st.divider()


# ---------------- ARRAY VISUALIZATION ----------------

st.subheader("Array Visualization")

chart_placeholder = st.empty()
display_chart(chart_placeholder, array)

st.write("**Current array:**")

array_placeholder = st.empty()
array_placeholder.code(str(array), language="python")


# ---------------- METRICS ----------------

st.subheader("Sorting Statistics")

metric_cols = st.columns(3)

comparison_placeholder = metric_cols[0].empty()
operation_placeholder = metric_cols[1].empty()
status_placeholder = metric_cols[2].empty()

comparison_placeholder.metric("Comparisons", 0)
operation_placeholder.metric("Swaps / Writes", 0)
status_placeholder.metric("Status", "Ready")


# ---------------- SORT BUTTON ----------------

if st.button("▶ Start Sorting", type="primary", use_container_width=True):

    working_array = st.session_state.array.copy()
    sorting_function = ALGORITHMS[algorithm_name]

    status_placeholder.metric("Status", "Sorting...")

    final_comparisons = 0
    final_operations = 0

    for current_array, comparisons, operations in sorting_function(
        working_array
    ):
        display_chart(chart_placeholder, current_array)

        array_placeholder.code(
            str(current_array),
            language="python",
        )

        comparison_placeholder.metric(
            "Comparisons",
            comparisons,
        )

        operation_placeholder.metric(
            "Swaps / Writes",
            operations,
        )

        final_comparisons = comparisons
        final_operations = operations

        time.sleep(animation_delay)


    st.session_state.array = working_array.copy()

    display_chart(chart_placeholder, working_array)

    array_placeholder.code(
        str(working_array),
        language="python",
    )

    comparison_placeholder.metric(
        "Comparisons",
        final_comparisons,
    )

    operation_placeholder.metric(
        "Swaps / Writes",
        final_operations,
    )

    status_placeholder.metric("Status", "Completed")

    st.success("Array sorted successfully! 🎉")
