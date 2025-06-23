import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

all_data = pd.read_csv('all_data.csv')

st.title('E-Commerce Data Dashboard')

st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Select a page', ['Overview', 'Customer Analysis', 'Order Analysis', 'Payment Analysis'])

if page == 'Overview':
    st.header('Overview of E-Commerce Data')
    st.subheader('Dataset Info')
    st.write('Number of records:', all_data.shape[0])
    st.write('Number of columns:', all_data.shape[1])
    
    st.subheader('Sample Data')
    st.dataframe(all_data.head())

    st.subheader('Summary Statistics')
    st.write(all_data.describe())

    st.subheader('Key Metrics')
    total_revenue = all_data['payment_value'].sum()
    total_orders = all_data['order_id'].nunique()
    avg_review_score = all_data['review_score'].mean()
    
    st.metric('Total Revenue', f"${total_revenue:,.2f}")
    st.metric('Total Orders', total_orders)
    st.metric('Average Review Score', f"{avg_review_score:.2f}")

    # Add review score distribution visualization
    st.subheader('Review Score Distribution')
    fig, ax = plt.subplots()
    all_data['review_score'].value_counts().sort_index().plot(kind='bar', ax=ax)
    ax.set_title('Review Score Distribution')
    ax.set_xlabel('Review Score')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Add orders per day visualization
    st.subheader('Orders per Day')
    all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])
    orders_per_day = all_data.groupby(all_data['order_purchase_timestamp'].dt.date)['order_id'].count()
    
    fig, ax = plt.subplots()
    orders_per_day.plot(ax=ax)
    ax.set_title('Orders per Day')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Orders')
    st.pyplot(fig)

elif page == 'Customer Analysis':
    st.header('Customer Analysis')
    
    if 'customer_state' in all_data.columns:
        customer_state = st.selectbox('Filter by Customer State', all_data['customer_state'].unique())
        filtered_data = all_data[all_data['customer_state'] == customer_state]
        st.write(f"Number of customers in {customer_state}: {filtered_data['customer_unique_id'].nunique()}")
        st.dataframe(filtered_data)
    
    if 'customer_state' in all_data.columns:
        st.subheader('Customer Distribution by State')
        customer_distribution = all_data['customer_state'].value_counts()
        st.bar_chart(customer_distribution)

elif page == 'Order Analysis':
    st.header('Order Analysis')

    st.subheader('Orders Overview')
    st.dataframe(all_data[['order_id', 'order_status', 'order_purchase_timestamp']].drop_duplicates().head())
    
    if 'order_status' in all_data.columns:
        order_status = st.selectbox('Select Order Status', all_data['order_status'].unique())
        filtered_orders = all_data[all_data['order_status'] == order_status]
        st.write(f"Number of {order_status} orders: {filtered_orders['order_id'].nunique()}")
        st.dataframe(filtered_orders)

    if 'order_status' in all_data.columns:
        st.subheader('Order Status Distribution')
        order_status_distribution = all_data['order_status'].value_counts()
        st.bar_chart(order_status_distribution)

elif page == 'Payment Analysis':
    st.header('Payment Analysis')

    if 'payment_type' in all_data.columns:
        st.subheader('Payment Types Distribution')
        payment_type_counts = all_data['payment_type'].value_counts()
        st.bar_chart(payment_type_counts)

    if 'payment_value' in all_data.columns and 'payment_type' in all_data.columns:
        st.subheader('Total Revenue by Payment Type')
        payment_revenue = all_data.groupby('payment_type')['payment_value'].sum()
        st.bar_chart(payment_revenue)
