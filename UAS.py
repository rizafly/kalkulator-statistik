import streamlit as st
import numpy as np
import pandas as pd

# Fungsi untuk menghitung statistik dasar
def calculate_statistics(data):
    return {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Mode": pd.Series(data).mode().tolist(),
        "Standard Deviation": np.std(data),
        "Variance": np.var(data),
        "Minimum": np.min(data),
        "Maximum": np.max(data),
        "Range": np.max(data) - np.min(data),
    }

# Judul aplikasi
st.title("Statistical Calculator")

# Input data
st.header("Input Data")
data_input = st.text_area(
    "Enter your data (separate by commas):", placeholder="e.g., 1, 2, 3, 4, 5")

if st.button("Calculate Statistics"):
    try:
        # Mengubah input menjadi list angka
        data = list(map(float, data_input.split(",")))

        if len(data) == 0:
            st.error("Please enter at least one number.")
        else:
            # Menghitung statistik
            stats = calculate_statistics(data)

            # Menampilkan hasil
            st.header("Statistics")
            for stat, value in stats.items():
                st.write(f"{stat}: {value}")

    except ValueError:
        st.error("Invalid input. Please enter numbers separated by commas.")