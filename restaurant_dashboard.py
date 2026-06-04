import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Restaurant Channel Profitability Dashboard",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("processed_restaurant_data.csv")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Filters")

selected_cuisine = st.sidebar.multiselect(
    "Cuisine Type",
    sorted(df["CuisineType"].unique()),
    default=sorted(df["CuisineType"].unique())
)

selected_segment = st.sidebar.multiselect(
    "Business Segment",
    sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

selected_channel = st.sidebar.selectbox(
    "Waterfall Channel",
    ["InStore", "UberEats", "DoorDash", "SelfDelivery"]
)

commission_rate = st.sidebar.slider(
    "Commission Rate (%)",
    min_value=10,
    max_value=40,
    value=30
)

delivery_multiplier = st.sidebar.slider(
    "Delivery Cost Multiplier",
    min_value=1.0,
    max_value=3.0,
    value=1.0,
    step=0.1
)

# =====================================================
# FILTER DATA
# =====================================================

filtered_df = df[
    (df["CuisineType"].isin(selected_cuisine))
    &
    (df["Segment"].isin(selected_segment))
]

# =====================================================
# TITLE
# =====================================================

st.title("Restaurant Channel Profitability Analysis Dashboard")

st.markdown("""
### SkyCity Auckland Restaurants & Bars

Compare profitability across:
- InStore
- Uber Eats
- DoorDash
- Self Delivery

Evaluate margin erosion, commission drag and delivery cost impact.
""")

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Profit Comparison",
    "Margin Analysis",
    "Cost Breakdown",
    "Cuisine & Segment",
    "What-If Analysis"
])

# =====================================================
# TAB 1
# =====================================================

with tab1:

    st.header("Channel Wise Profit Comparison")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "InStore Profit",
        f"${filtered_df['InStoreNetProfit'].sum():,.0f}"
    )

    col2.metric(
        "Uber Eats Profit",
        f"${filtered_df['UberEatsNetProfit'].sum():,.0f}"
    )

    col3.metric(
        "DoorDash Profit",
        f"${filtered_df['DoorDashNetProfit'].sum():,.0f}"
    )

    col4.metric(
        "Self Delivery Profit",
        f"${filtered_df['SelfDeliveryNetProfit'].sum():,.0f}"
    )

    profit_df = pd.DataFrame({
        "Channel": [
            "InStore",
            "UberEats",
            "DoorDash",
            "SelfDelivery"
        ],
        "Net Profit": [
            filtered_df["InStoreNetProfit"].sum(),
            filtered_df["UberEatsNetProfit"].sum(),
            filtered_df["DoorDashNetProfit"].sum(),
            filtered_df["SelfDeliveryNetProfit"].sum()
        ]
    })

    st.subheader("Total Net Profit by Channel")

    st.bar_chart(
        profit_df.set_index("Channel")
    )

# =====================================================
# TAB 2
# =====================================================

with tab2:

    st.header("Margin Analysis")

    margin_df = pd.DataFrame({
        "Channel": [
            "InStore",
            "UberEats",
            "DoorDash",
            "SelfDelivery"
        ],
        "Margin (%)": [
            filtered_df["InStore_Margin_Percent"].mean(),
            filtered_df["UE_Margin_Percent"].mean(),
            filtered_df["DD_Margin_Percent"].mean(),
            filtered_df["SD_Margin_Percent"].mean()
        ]
    })

    st.bar_chart(
        margin_df.set_index("Channel")
    )

    risk_df = pd.DataFrame({
        "Channel": [
            "InStore",
            "UberEats",
            "DoorDash",
            "SelfDelivery"
        ],
        "Volatility": [
            filtered_df["InStore_Margin_Percent"].std(),
            filtered_df["UE_Margin_Percent"].std(),
            filtered_df["DD_Margin_Percent"].std(),
            filtered_df["SD_Margin_Percent"].std()
        ]
    })

    st.subheader("Margin Volatility")

    st.dataframe(risk_df, use_container_width=True)

# =====================================================
# TAB 3
# =====================================================

with tab3:

    st.header("Cost Component Breakdown")

    cost_df = pd.DataFrame({

        "Revenue": [
            filtered_df["InStoreRevenue"].sum(),
            filtered_df["UberEatsRevenue"].sum(),
            filtered_df["DoorDashRevenue"].sum(),
            filtered_df["SelfDeliveryRevenue"].sum()
        ],

        "COGS": [
            filtered_df["InStore_COGS"].sum(),
            filtered_df["UE_COGS"].sum(),
            filtered_df["DD_COGS"].sum(),
            filtered_df["SD_COGS"].sum()
        ],

        "OPEX": [
            filtered_df["InStore_OPEX"].sum(),
            filtered_df["UE_OPEX"].sum(),
            filtered_df["DD_OPEX"].sum(),
            filtered_df["SD_OPEX"].sum()
        ]

    },

    index=[
        "InStore",
        "UberEats",
        "DoorDash",
        "SelfDelivery"
    ])

    st.dataframe(cost_df, use_container_width=True)

    st.subheader("Waterfall Chart")

    if selected_channel == "InStore":

        values = [
            filtered_df["InStoreRevenue"].sum(),
            -filtered_df["InStore_COGS"].sum(),
            -filtered_df["InStore_OPEX"].sum(),
            filtered_df["InStoreNetProfit"].sum()
        ]

        labels = ["Revenue", "COGS", "OPEX", "Profit"]

    elif selected_channel == "UberEats":

        values = [
            filtered_df["UberEatsRevenue"].sum(),
            -filtered_df["UE_COGS"].sum(),
            -filtered_df["UE_OPEX"].sum(),
            -filtered_df["UE_Commission"].sum(),
            filtered_df["UberEatsNetProfit"].sum()
        ]

        labels = [
            "Revenue",
            "COGS",
            "OPEX",
            "Commission",
            "Profit"
        ]

    elif selected_channel == "DoorDash":

        values = [
            filtered_df["DoorDashRevenue"].sum(),
            -filtered_df["DD_COGS"].sum(),
            -filtered_df["DD_OPEX"].sum(),
            -filtered_df["DD_Commission"].sum(),
            filtered_df["DoorDashNetProfit"].sum()
        ]

        labels = [
            "Revenue",
            "COGS",
            "OPEX",
            "Commission",
            "Profit"
        ]

    else:

        values = [
            filtered_df["SelfDeliveryRevenue"].sum(),
            -filtered_df["SD_COGS"].sum(),
            -filtered_df["SD_OPEX"].sum(),
            -filtered_df["SD_DeliveryTotalCost"].sum(),
            filtered_df["SelfDeliveryNetProfit"].sum()
        ]

        labels = [
            "Revenue",
            "COGS",
            "OPEX",
            "Delivery Cost",
            "Profit"
        ]

    fig = go.Figure(go.Waterfall(
    name="Profit Flow",
    orientation="v",

    measure=[
        "absolute",
        "relative",
        "relative",
        "relative",
        "total"
    ][:len(values)],

    x=labels,
    y=values
))

fig.update_layout(
    title=f"{selected_channel} Cost Waterfall",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# TAB 4
# =====================================================

with tab4:

    st.header("Cuisine & Segment Profitability")

    cuisine_heatmap = pd.DataFrame({

        "InStore":
            filtered_df.groupby("CuisineType")["InStore_Margin_Percent"].mean(),

        "UberEats":
            filtered_df.groupby("CuisineType")["UE_Margin_Percent"].mean(),

        "DoorDash":
            filtered_df.groupby("CuisineType")["DD_Margin_Percent"].mean(),

        "SelfDelivery":
            filtered_df.groupby("CuisineType")["SD_Margin_Percent"].mean()

    })

    st.subheader("Cuisine Margin Heatmap")

    fig1, ax1 = plt.subplots(figsize=(10,5))

    sns.heatmap(
        cuisine_heatmap,
        annot=True,
        cmap="RdYlGn",
        ax=ax1
    )

    st.pyplot(fig1)

    segment_heatmap = pd.DataFrame({

        "InStore":
            filtered_df.groupby("Segment")["InStore_Margin_Percent"].mean(),

        "UberEats":
            filtered_df.groupby("Segment")["UE_Margin_Percent"].mean(),

        "DoorDash":
            filtered_df.groupby("Segment")["DD_Margin_Percent"].mean(),

        "SelfDelivery":
            filtered_df.groupby("Segment")["SD_Margin_Percent"].mean()

    })

    st.subheader("Segment Margin Heatmap")

    fig2, ax2 = plt.subplots(figsize=(8,4))

    sns.heatmap(
        segment_heatmap,
        annot=True,
        cmap="RdYlGn",
        ax=ax2
    )

    st.pyplot(fig2)

# =====================================================
# TAB 5
# =====================================================

with tab5:

    st.header("What-If Analysis")

    simulated_ue_profit = (
        filtered_df["UberEatsRevenue"]
        - filtered_df["UberEatsRevenue"] * filtered_df["COGSRate"]
        - filtered_df["UberEatsRevenue"] * filtered_df["OPEXRate"]
        - filtered_df["UberEatsRevenue"] * (commission_rate / 100)
    ).sum()

    simulated_dd_profit = (
        filtered_df["DoorDashRevenue"]
        - filtered_df["DoorDashRevenue"] * filtered_df["COGSRate"]
        - filtered_df["DoorDashRevenue"] * filtered_df["OPEXRate"]
        - filtered_df["DoorDashRevenue"] * (commission_rate / 100)
    ).sum()

    simulated_sd_profit = (
        filtered_df["SelfDeliveryRevenue"]
        - filtered_df["SelfDeliveryRevenue"] * filtered_df["COGSRate"]
        - filtered_df["SelfDeliveryRevenue"] * filtered_df["OPEXRate"]
        - filtered_df["SD_DeliveryTotalCost"] * delivery_multiplier
    ).sum()

    simulated_instore_profit = (
        filtered_df["InStoreNetProfit"].sum()
    )

    simulation_df = pd.DataFrame({
        "Channel": [
            "InStore",
            "UberEats",
            "DoorDash",
            "SelfDelivery"
        ],
        "Profit": [
            simulated_instore_profit,
            simulated_ue_profit,
            simulated_dd_profit,
            simulated_sd_profit
        ]
    })

    st.subheader("Simulated Profit by Channel")

    st.bar_chart(
        simulation_df.set_index("Channel")
    )

    st.dataframe(simulation_df)