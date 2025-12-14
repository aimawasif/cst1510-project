import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(30,4),
    columns=["London","New YORK","tokyo","Dubai"]
)

st.line_chart(data)
