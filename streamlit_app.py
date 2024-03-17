import streamlit as st
import numpy as np
import pandas as pd

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
    
    for i in range (n):
        for j in range (n):
            if(solver[i][j]!=0.00):
                if(debt[j]<0.00):
                    solver[i][j]=min(debt[i], abs(debt[j]))
                    debt[i]-=solver[i][j]
                    debt[j]+=solver[i][j]
                else:
                    solver[i][j]=0.00
    st.write("To Settle the Amount")
    for i in range (n):
        for j in range(n):
            if(solver[i][j]!=0):
                st.write(data[i]["name"]," should pay ₹", round(solver[i][j], 2), " to ", data[j]["name"], ".")

st.title("Amount Splitter")

col1, col2=st.columns(2)
with col1:
    st.write("##")
    st.write("Enter the number of people")
with col2:
    n=st.number_input("",min_value=0, step=1)
name = []
amount=[]
data=[]
for i in range(n):
    col1, col2 = st.columns(2)
    with col1:
        tempName = st.text_input(f"Enter the name {i+1}")
    with col2:
        tempAmount =st.number_input(f"Enter the amount {i+1}",step=1.,format="%.2f")
        #amount = st.text_input(f"Enter the amount {i+1}", key=f"amount_{i}")
    #name.append(tempName)
    #amount.append(tempAmount)
    data.append({"name":tempName, "amount":tempAmount})

#for i in range(n):
#    st.write(data[i]["name"], data[i]["amount"])
#st.write(totalSpendings(data))
#viewData(data)
#st.write(perHeadExpenditure(data))
if(st.button("Settle Now") and n>0):
    if(n==1):
        st.write("No Need for settlement")
    else:
        settle(data)
