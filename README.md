# Exploration-of-E-Commerce-Transactions
The goal of this project is to document my learning process in discovering skills & tools for data analytics. <br>
I explored Kaggle for a dataset that picqued my interest: https://www.kaggle.com/datasets/steve1215rogg/e-commerce-dataset/data. <br>
This is a simple fictional dataset regarding a ledger of e-commerce transactions. <br>
It was a good mix of beginning with something manageable, working with practical data, and thinking about how to ask the right questions. <br>

# Excel
I opened up the dataset in excel, and it opened up with the following parameters: <br>
User_ID	| Product_ID	| Category	| Price (Rs.)	| Discount (%)	| Final_Price(Rs.)	| Payment_Method	| Purchase_Date <br>
The columns itself are straightforward, but I had two questions right off the bat:
- The User_ID field had both alphanumeric and just numbers as variables. Why?
  - I created a helper column(U_ID_isAlphaNumeric) to identify whether it was alphanumeric. My intuition is to use it to later assists with information gathering through pivot tables.
- The purchase dates had two different formats, one that used slashes, and the other that used dashes. Would I have to clean this up?
  - Excel may have converted some of the values from the CSV file to be text strings, which caused the inconsistency.
  - I cleaned it up for consistency sake by formatting the entire column as YYYY/MM/DD. 
