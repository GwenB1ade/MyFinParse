import streamlit as st
import pandas as pd

from parser.currency import get_best_currency, get_currency
from utils import convert_to_dataframe, convert_best_currency_to_dataframe




def main():
    df = convert_to_dataframe(get_currency())
    st.title('Курс валют в Гродно')
    st.dataframe(df, height = 700)
    st.title('Лучшие курсы:')
    best_df = convert_best_currency_to_dataframe(get_best_currency())
    st.dataframe(best_df)
    

if __name__ == '__main__':
    main()