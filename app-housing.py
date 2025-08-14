import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


st.title('California Housing Data (1990) by Luna Zhang')
df = pd.read_csv('housing.csv')

# median housing price slider
median_price_filter = st.slider('Median Housing Price ($):', 0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button widget
income_level = st.radio(
    "Choose income level",
    ["Low", "Medium", "High"],
)

if income_level == "Low":
    st.write("median income <= 2.5.")
    df = df[df.median_income <= 2.5]
elif income_level == "Medium":
    st.write("2.5 < median income < 4.5.")
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_level == "High":
    st.write("median income >= 4.5.")
    df = df[df.median_income >= 4.5]

# filter by median price
df = df[df.median_house_value >= median_price_filter]
# filter by location
df = df[df.ocean_proximity.isin(location_filter)]


# show on map
st.map(df)


# show the plot
st.subheader('Median House Value')
fig, ax = plt.subplots(figsize=(20, 5))
ax.hist(df.median_house_value,bins=30, edgecolor='black')
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)