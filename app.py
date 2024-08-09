import streamlit as st
import pickle
import pandas as pd

def Top_recommendation(product,confidence):
  # Convert 'antecedents' to strings for easier comparison
   rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
   rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))


     # Filter the rules using the 'antecedents_str' column
   recommendation = rules[(rules['antecedents_str']== product) & (rules['confidence'] > confidence)].sort_values(by=['confidence','lift'], ascending=False)
   return recommendation

def least_recommendation(product,confidence):
  # Convert 'antecedents' to strings for easier comparison
   rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
   rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))


     # Filter the rules using the 'antecedents_str' column
   recommendation = rules[(rules['antecedents_str']== product) & (rules['confidence'] > confidence)].sort_values(by=['confidence','lift'], ascending=False)[-10:]
   return recommendation

product_dict = pickle.load(open('antecedents_products_dict.pkl','rb'))
product = pd.DataFrame(product_dict)


rules = pickle.load(open('apriori_rule.pkl','rb'))

st.title('Product Recommender System')

select_antecedents = st.selectbox(
    'Enter the antecedents product',
    product['Product'].values)

st.title('Confidence%')
slider_value = st.slider('Select a value', min_value=0.0, max_value=1.0, step=0.01)


if st.button('Top_Recommend'):
    recomend= Top_recommendation(select_antecedents,slider_value)
    st.write(recomend)

if st.button('Least_Recommend'):
    recomend= least_recommendation(select_antecedents,slider_value)
    st.write(recomend)
