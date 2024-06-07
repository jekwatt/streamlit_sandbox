from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# Set up file paths using pathlib and __file__
base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data"
iris_path = data_path / "iris.csv"
media_path = base_dir / "media"


# text

st.title("What is Streamlit?")
st.image(str(media_path / "streamlit.png"))
st.subheader("Allows you to quickly build web applications and dashboards in Python")
st.write("---")


st.header("Iris Data!")

iris = pd.read_csv(iris_path)
st.write(iris)
st.write("---")


# Plotly

st.header("Plots")


# Scatter plot
st.subheader("Is the sepal length useful for classifying species?")

scat = px.scatter(
    iris,
    x="sepal_length",
    y="sepal_width",
    marginal_x="box",
    marginal_y="violin",
    color="species",
)
st.write(scat)
st.write("---")


# Bar plot
st.subheader("How many iris flowers of each species are in our dataset?")

species_counts = iris["species"].value_counts().reset_index()
species_counts.columns = ["species", "count"]

bar_fig = px.bar(
    species_counts,
    x="species",
    y="count",
    color="species",
    title="Number of Iris Flowers by Species",
    labels={"species": "Species", "count": "Count"},
    color_discrete_map={"setosa": "blue", "versicolor": "red", "virginica": "green"},
)
st.plotly_chart(bar_fig)
st.write("---")


# KDE plot (histogram)
st.subheader("Can petal width be used to distinguish the species?")

kde_fig = px.histogram(
    iris,
    x="petal_width",
    color="species",
    marginal="rug",
    histnorm="density",
    opacity=0.7,
    title="Petal Width Distribution by Species",
    labels={"petal_width": "Petal Width", "species": "Species"},
    color_discrete_map={"setosa": "blue", "versicolor": "red", "virginica": "green"},
)
st.plotly_chart(kde_fig)
