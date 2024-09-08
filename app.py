import streamlit as st
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def viewNodes(solver, n, data):
    edges = []
    for i in range(n):
        for j in range(n):
            if(solver[i][j]>0.0):
                edges.append((data[i]["name"], data[j]["name"]))
    
    G = nx.DiGraph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    num_nodes=len(G.nodes())
    base_node_size = 100
    node_size = max(base_node_size // num_nodes, 100)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=node_size, font_size=8, ax=ax)
    st.pyplot(fig)


def totalSpendings(data):
    moneySpent=0.00
    no=len(data)
    for i in range(no):
        moneySpent+=data[i]["amount"]
    return moneySpent

def viewData(data):
    n=len(data)
    for i in range(n):
        st.write(data[i]["name"], data[i]["amount"])

def perHeadExpenditure(data):
    n=len(data)
    moneySpent=totalSpendings(data)
    return moneySpent/n

def settle(data):
    n=len(data)
    perHead=perHeadExpenditure(data)
    debt = [0.0 for i in range(n)]
    for i in range(n):
        debt[i] = perHead - data[i]["amount"]
    
    solver = [[1.00 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(i==j):
                solver[i][j]=0.00
            elif(debt[i]<=0):
                solver[i][j]=0.0
    col1, col2=st.columns(2)
    with col1:
        st.header("Traditional Method")
        viewNodes(solver, n, data)
    for i in range (n):
        for j in range (n):
            if(solver[i][j]!=0.00):
                if(debt[j]<0.00):
                    solver[i][j]=min(debt[i], abs(debt[j]))
                    debt[i]-=solver[i][j]
                    debt[j]+=solver[i][j]
                else:
                    solver[i][j]=0.00
    with col2:
        st.header("Optimal Method")
        viewNodes(solver, n, data)
    
    st.subheader("To Settle the Amount: ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Whom should pay?**")
    with col2:
        st.write(f"**To whom should pay?**")
    with col3:
        st.write(f"**Amount**")
    
    for i in range (n):
        for j in range(n):
            if(solver[i][j]!=0):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text(data[i]['name'])
                with col2:
                    st.text(data[j]['name'])
                with col3:
                    st.text(round(solver[i][j], 2))


with st.sidebar:
    st.title("Expense Splitter")
    st.write("#")
    st.write("Enter the number of people (>1)")
    n=st.number_input("",min_value=0, step=1)
    st.markdown('😺 See Project Repository on [GitHub](https://github.com/iamsahilkansal/expense-splitter-app)')
    st.markdown('👨‍💻 Made by [**Sahil Kansal**](https://www.linkedin.com/in/iamsahilkansal/)')

name = []
amount=[]
data=[]
for i in range(n):
    col1, col2 = st.columns(2)
    with col1:
        tempName = st.text_input(f"Enter the name for person {i+1}")
    with col2:
        tempAmount =st.number_input(f"Enter the amount for person {i+1}",step=1.,format="%.2f")
    data.append({"name":tempName, "amount":tempAmount})
if(n>1):
    if(st.button("Settle Now")):
        if(n==1):
            st.write("No Need for settlement")
        else:
            settle(data)
