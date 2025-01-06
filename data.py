import pandas as pd
import plotly.express as px
import streamlit as st

# --- Streamlit App Title ---
st.title("Tesla Data Analysis Dashboard")
st.write("Analyze Tesla's stock data with comprehensive visualizations and insights.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload the Tesla dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # --- Data Preprocessing ---
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Convert 'Date' column to datetime if available
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    st.write("### Summary Statistics")
    st.write(df.describe())

    # --- Data Visualizations ---
    # 1. Line Chart: Close Price Over Time
    if 'Date' in df.columns and 'Close' in df.columns:
        st.subheader("Close Price Over Time")
        fig_line = px.line(df, x='Date', y='Close', title="Tesla Close Price Over Time")
        st.plotly_chart(fig_line)

    # 2. Scatter Plot: Volume vs. Close Price
    if 'Close' in df.columns and 'Volume' in df.columns:
        st.subheader("Volume vs. Close Price")
        fig_scatter = px.scatter(df, x='Close', y='Volume', color='Volume', title="Volume vs. Close Price")
        st.plotly_chart(fig_scatter)

    # 3. Histogram: Close Price Distribution
    if 'Close' in df.columns:
        st.subheader("Close Price Distribution")
        fig_hist = px.histogram(df, x='Close', nbins=30, title="Distribution of Close Prices")
        st.plotly_chart(fig_hist)

    # 4. Bar Chart: Average Close Price by Year
    if 'Date' in df.columns and 'Close' in df.columns:
        st.subheader("Average Close Price by Year")
        df['Year'] = df['Date'].dt.year
        avg_close_by_year = df.groupby('Year')['Close'].mean().reset_index()
        fig_bar_year = px.bar(avg_close_by_year, x='Year', y='Close', title="Average Close Price by Year")
        st.plotly_chart(fig_bar_year)

    # 5. Pie Chart: Volume Distribution by Year
    if 'Year' in df.columns and 'Volume' in df.columns:
        st.subheader("Volume Distribution by Year")
        volume_by_year = df.groupby('Year')['Volume'].sum().reset_index()
        fig_pie = px.pie(volume_by_year, names='Year', values='Volume', title="Volume Distribution by Year")
        st.plotly_chart(fig_pie)

    # 6. Box Plot: Close Price by Year
    if 'Year' in df.columns and 'Close' in df.columns:
        st.subheader("Close Price Distribution by Year")
        fig_box = px.box(df, x='Year', y='Close', title="Close Price Distribution by Year")
        st.plotly_chart(fig_box)

    # 7. Time Series: High vs. Low Prices
    if 'Date' in df.columns and 'High' in df.columns and 'Low' in df.columns:
        st.subheader("High vs. Low Prices Over Time")
        fig_high_low = px.line(df, x='Date', y=['High', 'Low'], title="High vs. Low Prices Over Time")
        st.plotly_chart(fig_high_low)

    # 8. Heatmap: Correlation Matrix
    st.subheader("Correlation Matrix")
    if len(df.select_dtypes(include=['float', 'int']).columns) > 1:
        corr_matrix = df.corr()
        fig_heatmap = px.imshow(corr_matrix, text_auto=True, title="Correlation Matrix")
        st.plotly_chart(fig_heatmap)
    else:
        st.write("Not enough numerical columns for Correlation Matrix.")

    # 9. Bar Chart: Total Volume by Month
    if 'Date' in df.columns and 'Volume' in df.columns:
        st.subheader("Total Volume by Month")
        df['Month'] = df['Date'].dt.month
        volume_by_month = df.groupby('Month')['Volume'].sum().reset_index()
        fig_bar_month = px.bar(volume_by_month, x='Month', y='Volume', title="Total Volume by Month")
        st.plotly_chart(fig_bar_month)

    # 10. Area Chart: Adj Close Price Over Time
    if 'Date' in df.columns and 'Adj Close' in df.columns:
        st.subheader("Adjusted Close Price Over Time")
        fig_area = px.area(df, x='Date', y='Adj Close', title="Adjusted Close Price Over Time")
        st.plotly_chart(fig_area)

    # --- Interpretations ---
    st.subheader("Key Insights")
    st.write("""
    1. **Close Price Trends**: Observe the overall performance of Tesla's stock over the selected timeframe.
    2. **Volume Trends**: High trading volumes often correspond to significant price changes or events.
    3. **Yearly Patterns**: Use average close prices by year to identify trends and growth.
    4. **Volatility Analysis**: Box plots show how much the stock price fluctuates yearly.
    5. **Correlation Analysis**: Understand relationships between features like Volume, Close Price, and others.
    """)

else:
    st.write("Please upload a dataset to proceed.")
