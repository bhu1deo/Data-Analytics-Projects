The files outline some of my Experience working with Pivot Tables/Power Pivot and Power Query. 
Excel Pivot Tables Important Topics/Points: 

- Filters, Columns, Rows and Values
- Pivot Table Analyze -> Add a new Calculated Field
- Design Tab -> Different type of Report Layouts
- Right Click on entries in a pivot table column and then do show values as: different Table Calculation Options are available. % of Column, % of Parent, etc. 
- Sort, More Sorting Options, Value Filters & Label Filters in the Dimension Column of the Pivot table. 
- For % formatted columns, when the table is indifferent to Value filters based on another column, then provide the threshold values in decimal points. 
- By default Pivot Table would allow only one filter on a column. Can change that by going to Analyze and Options and Totals and Filters, impose multiple filters on a field option.
- Rather than Sum, sometimes we might interpret better with the Average metric. 
- Right Click on the fields in any column and then change the Aggregation: Summarization By->. Default summarization mode in Pivot tables is SUM. 
- Group some of the dimension values together: In case of overlapping/related values. Right click (after selecting the values) and then Group.
- Manually scrolling through and grouping values could be cumbersome. We can instead create a lookup table and then use lookup functions in order to see group of fields. 
- Select values in a column in the Pivot table: then right click and keep only selected items. 
- Pivot Table Tools -> Options and then deselect the AutoFit Column Width option. 
- Pivot Table Analyze Options -> Pivot Chart 
- Data which grows over time (stock market data): New rows get added below the original data: Give column only references. Or convert range to a Table (auto. Absorbs data). 
- Pivot Table Analyze : Group Ungroup options are available. 
- Select the entire chunk of data which we want to apply conditional formatting on: Go to Home and then Conditional formatting and then choose the formatting option. Highlight cell rule for colouring cells with a conditional rule. 
- ;;; : Removes the Numbers. (Blank Formatting), data bars can be inserted from conditional formatting as well. 
- Manage rules option in conditional formatting helps to edit and manage the formatting imposed. 
- Pivot Table Analyze-> Pivot Chart-> Combo chart : For dual axis different charts (for example a line chart and a column chart in the same visual). 
- Summarize Values By & Show Values as: After Right clicking on Entries inside a particular column.
- Very Imp: Calculated Fields in Excel Pivot Table default to SUM aggregation and that cannot be changed. Instead use custom calculations to get proper Averages. 
- We cannot add COUNT columns in our Calculated Field calculation: Because we need SUMs in the calculation. Rather we can have a Number of Records column and then SUM it up to get a COUNT Measure which can be added to the calculated field calculation. 
- Always any fields used in the Calculated Field calculation default to (and cannot be changed) SUM aggregation.
- Suppose you have a formatted column in your Excel Pivot Table: Now: You want to copy the formatting (conditional or normal) to other columns, then 1.) Select  the values in your formatted column 2.) then double click on **Format Painter** option in the Home Toolbox 3.) Click on the first cell in any other column to which you want to copy the formatting. 
- Format Painter is quite useful: it can even help you with field formatting like number formats applied to a particular column can be replicated to other columns as well. 
- See the automatically generated column headers to confirm the Aggregation used. 
- Pivot Table Analyze: Select Entire Pivot Table, and then copy paste. 
- Calc. Field : Always SUM Aggregation. Their Aggregation type cannot be changed. 
- To COUNT the number of rows in a table: One can just pull any of the dimensions present in that table into the Values field of the pivot table. This will apply the default COUNT aggregation and return the number of rows in the Pivot Table. 
- Select Pivot Chart. Go to Analyze and In the Field buttons dropdown: Hide field buttons. 
- If we have blank/non-numeric data in our columns, then when fields are dragged into our values shelf, then they may have a default COUNT aggregation. One can see the Column header as well as the aggregation type used in the Values shelf. They changes can be made if required. 
- We can modify existing calculated fields in the same dialog box (as adding a new one was). 
- To hide data from a column: either we can format as ;;;. Or we can go to conditional formatting (for data bars), and then show bars only. 
- Clear and Manage rules Conditional formatting: Home Tab. 
- Home Tab: Wrap Text in order to put your Excel Text on Multiple lines, rather on a single long line. 
- After a pivot chart is added: Go to pivot chart Design tools and then add a chart element: Add a trendline on Log scale. Then we can right click and then format the axis. 
- Value fields can also be grouped: The group can be provided with a starting point, an ending point and the group jump as well. 
- Averages and COUNT columns: 

Power Query & Power Pivot: (Load Data into Power Query: and then keep it ready for future processing (ETL processes)). Then use Power Pivot in order to Analyse the Data.

**Connect**    Make connections to data in the cloud, on a service, or locally.

**Transform**    Shape data to meet your needs, while the original source remains unchanged.

**Combine**    Integrate data from multiple sources to get a unique view into the data. (Append and Merge)

**Load**   Complete your query and load it into a worksheet or Data Model and periodically refresh it.

- Crucial: Data Tab-> Get & Transform Data. (Launch the Power Query Editor)
- Queries & Connections Pane, to see the Queries and Connections. 
- Then in the Queries & connections Pane we can right click and launch the Edit Query editor to manage our Queries. 
- The gear icon present for the Queries in the Query editing pane helps us to Edit & Manage Our Applied Queries. 
- If new data is added to contiguous rows/columns and our original data is formatted as a Table, then the newly added data gets automatically assimilated into the Table. Else we could drag completely; (new data) so that it aligns continuously with the original data (which is formatted as a table). 
- Can import all files from a folder: can exclude certain types of files: for example, we can import only xlsx files. Can combine all the imported files. Can load only as a Connection.
- As more files of existing type are added to the folder or even removed, the data updates automatically after refresh. 
- Pivoting/Unpivoting: If we select a set of columns and then do unpivot columns: then if some more columns are added later which need to be unpivoted: then we may face a problem. So, we may try to unpivot other columns at the outset. 
- Refresh works very well, when the underlying data is formatted as a Table and new columns/rows are added and assimilated in it. 
- Concept of Pivoting/Unpivoting is quite Important. 
- Left Anti Join: to keep information present only in the 1st Table. Common information would be removed. Compare information and then keep only information present in the first table!!!
- Transform Tab: Fill button and then fill down: The Null values would be replaced by values above it. Replacing NULL values!!!
- If while type conversion for dates: we get errors then: we should see our locale settings and then retry. 
- Using locale setting is also available in the Power Query Transform tab change settings option!!! Rather than adjusting your Excel locale settings: we can change the data type by using locale for that particular column only. 
- If we want to make copies of the query and then each one is slightly different from the other, then we can right click and duplicate the Query, in order to save effort. 
- Reference vs Duplicate Existing queries: (In the Query editor: queries pane in the left) Duplicate will apply all the steps from the start to the new tables. Reference will just create an independent reference (new query which can independently modified), of the original one, rather than duplicating the Query itself. 
- Analyse data across multiple tables, analyse large amount of data. 
- Data Model: 
- Power Pivot-> Manage: Core Power Pivot Experience
- Import Data from Database/Data Service/ Existing Connections
- Establish relationships on the basis of Keys. 
- Home Tab-> Diagram View. Then we see the tables being loaded up into the relationship view. 
- After the relationships have been defined: you Can go back to the data view. 
- So, in the View toolbox in our Power Pivot Manage: we have Data View (like Power Query do data manipulations and add Columns), Diagram View (establish relationships), Calculations Area (Measures).
- Calculation Area in the cells at the bottom of the Table: Can add Measures using := Operator. Everything is just like Power BI. 
- Power Pivot Toolbox in the original Excel workbook: Manage and Measures and KPIs and other options are available. 
- Better to add a Measure in the Power Pivot Manage view. 
- Just Like in Power BI: Measures can be divided to get a New Measure. No tension of default aggregation being SUM as in the case of Calculated Fields in Excel.
- Now Insert a Pivot from the data model we created!!!, instead of a Table/Range as we do in traditional analysis. 
- Standard Pivot Table: 1 table, Power Pivot-> Multiple Tables. 
- Power Pivot Prompt (in the toolbox) :-> New KPI, after adding the KPI we see 0s 1s and -1s, and new fields in the Toolbox at the right side (Pivot Table Fields), from there we could remove and then re-add the fields to see the icons. 
- Insert Slicer-> All (some tables might not be listed in the slicer menu as they have not been brought in to the pivot table view). 
- So ETL can be carried out in Power Query, then we can establish relationships and ananlyze data using Power Pivot.






