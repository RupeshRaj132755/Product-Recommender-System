import streamlit as st
import pickle
import pandas as pd

def Top_recommendation(product):
  # Convert 'antecedents' to strings for easier comparison
   rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
   rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))


     # Filter the rules using the 'antecedents_str' column
   recommendation = rules[(rules['antecedents_str']== product) & (rules['confidence'] > 0.10)].sort_values(by=['confidence','lift'], ascending=False)[1:10]
   return recommendation


product_dict = pickle.load(open('antecedents_products_dict.pkl','rb'))
product = pd.DataFrame(product_dict)


rules = pickle.load(open('apriori_rule.pkl','rb'))

st.title('Product Recommender System')

select_antecedents = st.selectbox(
    'Enter the antecedents product',
    product['Product'].values)

if st.button('Recommend'):
    recomend= Top_recommendation(select_antecedents)
    st.write(recomend)
