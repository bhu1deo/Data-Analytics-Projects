**POWER BI key points:**

- Options & Settings: Preview Features, Data Load, Regional Settings
- Report, Data and Relationships Views
- Connect, Shape & Transform data
- Build relationships
- Design Interactive reports
- All the tabs in the Access Toolbar
- Types of Data Connectors
- The Query Editor (Transform Data) Tabs available at the Top
- Creating a Rolling Calendar
- Index & Conditional Columns
- Grouping and Aggregating Data
- Pivoting & Unpivoting 
- Merging & Appending Queries
- Modifying Queries: Query History
- Data Category for geographical data types
- Hierarchies
- Importing fully built models from Excel
- Data Transformations : Headers, Data types, NULL values, TRIM, importing files from a folder, disable report refresh for static sources, only load required data
- Data model: relationships
- Database normalization
- Data Tables (Fact Tables), Lookup Tables
- Primary & Foreign Keys
- Merging tables conflicts with database normalization
- Manage relationships 
- Star schemas and Snowflake Schemas
- Active and Inactive Relationships
- 1-\* CARDINALITY
- Filter Flow and Bidirectional Filters
- Two Way Filters
- Two Way Filters and Ambiguous relationships
- Hiding Fields to prevent invalid Filter context
- Lookup Tables generally Above Data Tables
- DAX: Calc Columns and Measures 
- Implicit and Explicit Measures (prefer Explicit Measures)
- Understanding Filter Context and How Each Value is being computed 
- DAX functions & Operators
- RELATED function 
- COUNT function and it’s variations
- CALCULATE function
- ALL 
- FILTER
- X functions (Iterator functions like SUMPRODUCT in Excel): Row level functions 
- TIME Intelligence Formulas: YTD, Prev Period, Running Total
- Measure Trees
- Power BI report view: Filters, Tabs in the Access toolbar, Viz. Drill Through, Fields, Formatting, Analytics, Buttons, Bookmarks, Navigation, Report Interactions, Parameters
- Row Level Security, Layouts, Analytics, AI visuals
- Grain in the view: According to the dimension row values (and other applied filters), first the corresponding rows in the table are filtered, only then the aggregation takes pace to give the Measure value.  

Prepare bookmarks accompanied with buttons to go to pages. 

Data pre-processing: Trim leading and Trailing spaces from text based key fields. 

**Power BI Adventure Works Dataset Project:** The main aim of the project is to analyze the health of the company. A summary page should indicate the overall Revenue, Orders, Profit. It should also show the broad category-wise splits for the above metrics. Brief product-level information should be succintly detailed via appropriate visualizations. In the Product-level details page, individual product perfromance should be described. The metrics used for the description could be profit, returns, orders over time. Geographical, regionwise potential of the company should be shown on a map and conclusions should be drawn from it. Customer-level page should specify recurring customers, age-split of customers, most valuable customers and segmentation according to Age, Income, Occupation should be carried out.  

Data Analysis and Pre-processing: 

1) **The Dataset:**  We have a relational dataset at hand to be connected on the basis of keys. This is a classic dataset based upon a fictitious company selling bicycle and allied products. We have 7 tables: calendar, category, customer, product, returns, sales, subcategory, territories. 
   1. Sales: This is a data (fact) table. Sales concerning a product. Relationships: (and associated foreign key)
      1. To Calendar Table: Order date 
      1. To Product Table: Product Key
      1. To Customer: Customer Key
      1. To Territory: Territory Key

It also has Order Number, Order Line Item (distinguishing multiple items in the order and their order quantities). 

1. Returns: This is also a data (fact) table. Returns Information can be derived. Relationships: (a and associated foreign key)
   1. To Calendar table: Via Return Date
   1. To Territory: Via Territory Key
   1. To Product: Via Product Key

It also has Return Quantity for a particular product key (only differentiated by date and territory key), but we cannot deduce which customer was responsible for the return. It may happen that two different customers, or the same customer may return more than one quantity of a particular product (from the same territory and at the same date), but such cases cannot be separated from each other as no relationship can be established to the Customer Table. 

1. Product, Customer and Territory: These are lookup tables containing primary keys. 
1. Calendar: This is also a lookup table; this was constructed by using common date related functions operating on raw date values in Power BI. 
1. Subcategory and Category tables: These tables are also lookups. They are connected via Snowflake schemas (through the Product Table), to our data tables. 
1) Pre-processing: Headers, Data types, TRIM char values, date data types, geographical regions. Adding custom columns. Merging, Splitting, Grouping, Text based operations. 

Outcomes: 

1) Major chunk of profit for the company comes from bikes sales, amounting to $17M, (41% of Revenue). Accessories and clothing record $569K, (63%) and $161K, (44%). So, the company must dedicate considerable resources towards bike products. This includes ensuring the return rates are low, swift servicing/repairs, customized products, readily available spare parts, prompt customer service, pick up and delivery of bikes, inventory management.  
1) Mountain bikes occupy the top 5 spots as far as profit is concerned. Road and Touring bikes register substantially higher return rates, poorest being 15% for Road-650 Red, 52. Touring-2000 Blue, 46 registers a return rate of 7.5%, the worst in its category. High return rates are problematic, especially when a product has lot of orders, leading to a heavy load on the operation activities. 
1) The company has expansion opportunities in Canada, North America and Europe. It can look to combat competition and increase its outreach in already established customer bases of US and Australia. 
1) Revenue and Orders have been growing steadily, but so is Number of Returns. The company should hire additional staff, allocate more resources, coordinate with suppliers, strengthen supply chains in order to cater to the increasing demands. 
1) Long-term relationships should be built with recurring customers. They can be presented special services, offered additional discounts. Their suggestions could be useful to improve products and design custom-based ones. 
1) The company operates in the high-ticket segment, where products are expensive. Consequently professionals, skilled manuals, management employees place most orders. Similarly, quinquagenarians and people aged above place a large % of orders. The company can add more affordable products to attract Vicenarians and Tricenarians, leading to a better tomorrow. 
1) AI visuals: The key influencers visual helps us understand the factors affecting a particular outcome. For example, we could interpret the total profit based upon Current Age of our customer. And we obtain a bell curve. 
1) The Q&A visuals could be trained to identify synonymous words in a Natural language query. 

**Financial Data Analysis: Loan Default:** 

Data Analysis and Pre-processing: 

1) **The Dataset:** We have 8 tables: loan, order, trans, card, disp, client, account, district. 
   1. loan: loan\_id is the primary key. Account number on which the loan is taken. Duration of the loan, it’s issue date, amount and monthly payment. **Status** of the loan: (A: finished repaid, B: finished defaulted, C: unfinished w.r.t the date limit we have but repaid later, D: unfinished defaulted).
   1. trans: trans. Id, account related to that transaction, balance, date of trans, type and mode of operation.
   1. disp: client\_id, account\_id and type of the account: whether the holder is an owner or a disponent.
   1. Client: client information, birth date, district, gender.
   1. Card: card\_id, type of card, disp\_id.
   1. Account: district, account, frequency of operation.
   1. Order: order\_id, account, amount, symbol.
   1. Dist: district information
1) Pre-processing: Headers, Data types, TRIM char values, date data types, geographical regions.


Questions: 

1) The aim is to help the bank to better manage its loans, find risky clients among prospective ones, analyse demographics of loanees, transaction related information. 
1) Find: % of loans which have defaulted. Convert Czech Words to their English meanings. Do it for completed loans only (A vs. B). Label B loans are the bad loans. 
1) Minimum account balance before issuing the loan. 
1) Average Income and Expenditure before issuing the loan.
1) Loan amount issued as a % of the Average Income for good and bad loans.
1) Find for bad loans, on an average how many EMIs are paid before an EMI is missed. Find Average account balance before a loan is issued. The EMI is due on the 12th of Every month. Find the number of times (before the loan is issued) the account balance falls behind the EMI value (both for good and bad loans). 
1) Find the Income and Expenditure patterns for good and bad loans. 
1) Work on A vs. B loans: Good and Bad Completed Loans: Categorical variables. For each type of loans prepare dashboards: segmented by type of card issued, different nature of transactions, average account balance before the loan was issued, minimum account balance before the loan was issued. Minimum and average Balances after the loan was issued. 

Outcomes: 

1) Most loans are indeed repaid on time, good signs for the bank. 
1) The number of loans disbursed in increasing every year. Check for minimum account balance (MAB) before loan issue. Bad loans have a higher tally of negative MAB. Average bad loan amount is higher as compared to good loan amount.  So, forecasting risk behind an issued loan is important. Negative MAB before issuance of a loan should ring alarm bells. High capital borrowers should be critically evaluated based on their ability to repay the loan.
1) It is observed, on an average the disparity between Income and Expenditure (before issuance of the loan) for "good" borrowers is more as compared to "bad" borrowers. Check for client's Income and Expenditure through the transaction statement. Surplus is beneficial, whereas a deficit may be adverse.
1) Clients who apply for a credit card are more likely to repay their loans than those who do not. Credit card users are more accustomed to paying EMIs on time, as it can detract their credit score as well as attract a penalty.
1) Prague and parts of Bohemia are well off, hence a lower % of bad loans from these regions. Clients from Moravia should be further scrutinized before loan approval.
1) Only 4% (3/76) of Bad loans have Avg. monthly deficit (Income-Expenditure) higher than their EMI payments, in contrast to nearly 16% (95/606) for good loans. Managers should check for re-payment capability of clients who apply for loan.
1) Our insights were confirmed by the Key Influencers AI visual. 

Identifying traits of the top defaulter

First we apply account\_id filter to all the pages (report level filter), account\_id = 8566. Now we observe the following traits:

- Highly negative average monthly deficit (-2K) before loan issue, hence inability to pay EMIs on time. 
- Belongs to the underdeveloped region of Moravia. 
- Nearly break-even w.r.t Income and Expenditure before loan issue.
- Did not issue credit card. 
- Minimum balance before loan issue is negative. 
- Has missed a lot of EMIs. 

All these points comply with our analysis and are in accordance with identifying high risk customers for this dataset. 

The report level filter maybe cleared after discerning the above information.




