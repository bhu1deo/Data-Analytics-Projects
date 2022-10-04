**Tableau Summary :** 

- Import Data Source and Data Source Transformations 
- Data Interpreter for CSV and Excel
- Data Source Filters 
- Relationships between datasets in a relational database
- Changing column types, transforming data -> Split/Group etc. 
- Joins/Relationships and Blending 
- Live Connection and Extracts 
- Opening and Saving Tableau Public 
- Dimensions and Measures 
- Discrete and Continuous 
- Axis Sort ToolBar Sort and Field Sort
- Grouping Data : Always Dimensions Field Grouping and View Grouping Static 
- Sets : constant and computed 
- Creating Hierarchies 
- Tableau Filters and Order of Operations 
- Filter Shelf
- Date Filters : Latest Date To handle live/dynamic data 
- Filter Card Modes & Show Filter Option & Filter Customization
- Apply Filter Options (to this sheet or all sheets, etc.)
- Context Filters Dependent Top-N filter 
- Measure Filters 
- Date Filters : Relative Dates & Anchor Date & Filter to Latest Date when opened 
- Marks and their qualities 
- Dual Axis & Sync Axis & Hide Axis 
- Innermost fields and Outer Fields 
- Stacking Marks
- Pages Shelf and Playback Controls 
- Analytics Pane
- Viz. in tooltips
- 4 step process to get the Viz. you want 
- Constructing a Donut chart 
- Calculated Fields 
- Table Calcs Basic Calcs LOD Expressions 
- LOD Expressions and Aggregations 
- LOD : Include Exclude and Fixed 
- Table Calculations : Ranking/Recursion/Moving Calculations and Inter-Row calculations 
- Direction and Scope of Table Calcs : Partitioning and Addressing Fields 
- Parameters and Uses & Customization 
- Dashboard & Layout & Objects 
- Tiled vs Floating 
- Dashboard Sizing 
- Workbook, Worksheet, Field and Number Formatting 
- Transparent Sheet and Action Filters 
- Device Designer 
- Dashboard Stories 

**Dataset-1:** 

Tableau Project Dataset and Details: We have a superstore dataset at our hand. We have sales, profit, discount, returns as our measures. We also have some qualitative dimensions. 

Questions:

- Month Over Month Revenue Growth (Table) 
- Running Sum of Revenue (Line Chart) 
- Quarterly Revenue Growth (Table)
- YOY Revenue and add % diff from in it 
- Top-5 states driving Yearly Revenue (Buttonize, select a Year and then the button should lead to the top-5 states sheet)
- Average Revenue Per Order Trend 
- Factoring Returns in Revenue Computation 
- Top Profit-Making Segments Donut Chart 
- Relation between Discount and Sales 
- Top-10 customers driving Yearly Revenue (Buttonize, select a Year and then the button should lead to the top-10 sheet which should show from where the customers hail from, their sales, their profits and their returns). 
- Regions in the Map which make the most losses 
- KPI Cards: Selected Month Sales and Profit. Preceding Trends. 
- In the KPI card: Show Yearly Sales and Profit along with the trends. Also show monthly sales and profit along with the trends. 
- On the Map Display the Sales values and colour the map by the profit measure. 

Outcomes: 

- Good trend of YOY Revenue and Profit Increase. 
- Strong Seasonality and Regularity observed in the Sales Revenue trend. Q4 performs the best, while Q1 fares the worst. 
- Measures to improve Average Revenue per Order could be formulated. 
- Texas, Illinois, Ohio, Florida, Colorado were the worst performing states. The profit % was negative and heavy losses were reported in these states. 
- Consumer-> Corporate -> Home Office: Trend in the Profit-making segments. 
- In the Home Office segment: Particular months of the year consistently fared worse than with respect to the number of orders (Less than Average Orders). 

**Dateset-2:** 

IPL 2017 Data: Before joining on any text based fields : be sure to trim the fields of any trailing and leading spaces. Establish proper relationships in the dataset. Check Datatype of Identified columns. Filter to 2017 matches using Data source filters. 

Questions: We want to find out what the winning team did right. Also we are interested in finding out where did it go wrong for the losers.

- Find the top-5 batsman and the number of Runs Scored by Them, their strike rate, their average. Also Display their Team.
- Do the Same for Bowlers (Wickets, Avg. Economy). Segment by Pace vs Spin. Also Segment by left-arm vs right arm. Also Display their Team.
- Find the Team which won the highest number of matches. Check whether they are the eventual champions. Rank compared to other teams based on the following metrics: Runs scored in first 6 overs, middle overs and the final flourish. Wickets picked up in first 6 overs. Runs conceded in the final flourish. 
- Find the relation between wins and the toss and wins. Also find the preferred decision after winning the toss (field/bat). 
- Factors Affecting Loss For the Team which carried the wooden spoon (RCB 2017). 
- Bowlers and Batsman in top-10 for each of the Teams. 
- Wins of a Team as a ratio of total games played. Do the same when the Team bats first and fields first. 

Calculations, Filters, Visualizations:

- Data Source Filters : Limit to IPL-2017 dataset. DL matches are not being considered. So the results may vary in comparison with cricbuzz/espncricinfo. 
- NULL values are discarded wherever necessary. 
- Toss Sheet: 
  - Find the first fielding and first batting teams. Find out whether the first fielding team wins. Split by whether the first fielding team wins or loses. 
- Batting Stats: Dimension is Batsman Revised Out: A **special column** to deal with cases **when batsman is at the non-strikers end and he gets out**. Otherwise, these OUTs are missed in the calculation. Top-10 filter applied. 
  - Number of Times Batsman Dismissed: COUNT of the player dismissed column. 
  - Batsman NOT-OUTs: [Total Batsman Innings]-[Number of Times Batsman Dismissed].
  - Highest Score: For every Match get batsman score. Then take MAX over all the matches. 
  - Balls Faced: Discount Wide and No-Balls from COUNT of [Ball] calculation. 
  - Hundreds Scored: For every Match get batsman score. Then do a COUNT over scores for scores>=100.
  - Fifties Scored: Similar to Hundreds, COUNT scores in range 50-100.
  - 4’s HIT: COUNT of batsman runs, filter in range 4-6. (Exclude 6)
- Team Stats Batting: Batting Team is the segregating dimension. 
  - Team Wins: Add a winner column and COUNTD when Batting Team=Winner. 
  - Run Rate first 6 overs: 6\*[Total Runs Scored first 6 overs]/[Total Balls Played First 6 overs]
  - Wickets lost first 6 overs: [Total Runs Scored first 6 overs]/[Matches Played]
- Bowler Stats: Dimension is the Bowler. Top-10 filter applied.
  - Wickets Taken: COUNT of player dismissed when the player is not Run Out or Retired Hurt or Out Handling the Ball. 
  - Runs Conceded: SUM of [Total Runs]
  - Maiden Overs: For every Over bowled, SUM([Total Runs]), if it is equal to 0, then increment the COUNT by 1. 
  - Best Bowling Figures: For every Match, find the Number of Wickets taken, and do a MAX over it. Further, after the MAX wickets in a match are found out, find minimum runs conceded in matches where [Wickets Taken]=[MAX Wkt. Taken]
  - Number of Times Wkts. >=3: For every match find the number of wickets taken and COUNT how many times it is >=3. 
- Batting 1st vs 2nd Wins: Dimension is the [Team] column. 
  - Team Games Batting First: We already have [Batting First Team] and [Fielding First Team] columns. As our dimension is the [Team] column: When [Team] equals [Batting First Team], then do a COUNTD of ID. (We can also do a more complicated calculation avoiding the generated calculated columns.)
  - Team Games Won Batting First: Find If Team is also batting first and is also the Winner of the game. (We have a winner column at our disposal)
- Team Bowling Stats: All Measures are computationally easy. 
- Team Stats 1st vs 2nd : Dimensions are Team and Over group. (first 6, middle, last 6)
  - Team Run Rate 1st Innings: We compute the Average RR for each team. To compute the Average, we use in-formula computation. So first we include Match ID in our computation grain. Then we check whether [Team]=[Batting Team] & [Innings]=1. For all such instances, we sum the [Total Runs] scored. For all such instances we also store the Balls played. Division of the two quantities gives us the desired result. 
  - Team Wickets Taken 1st Innings: Average wickets taken segmented by the group of Overs. Find out the (COUNT of player dismissed) the wkts taken when [Team]=[Bowling Team] and [Innings]=1, then divide by number of such innings (COUNTD([Match Id])).
  - Global RR 1st Innings: Our grain in the view consists of Team and Over group as the dimensions. So, in order to compute a global Measure: We resort to FIXED calculation, disregarding Team. So, over the Over group grain, we compute 1st innings Total runs and divide by global total number of matches played in IPL-2017. 
- In retrospect, the 1st two calcs. could be simplified by computing over the default grains in the view: Team and Over group, no need to include [Match Id] in the calculation.

Outcomes: 

- Created a Story for the constructed visualizations. 
- Some conclusions drawn from the analysis are: 
  - Teams have a propensity for fielding first. A score on the board to set sights on, is better than runs to bank upon.
  - Result is slightly tilted in favour of the chasing Team.
  - One can't rely on the toss if he aims to lift the title.
  - GL and RCB languish at the bottom with worst % wins ratios. The former cannot defend and the latter cannot chase targets. VK's atrophied powers add to RCB's misery. MI (Champs) do well irrespective of the toss.
- **MI:** Middle Overs is a Problem. Too much left for the likes of Pollard and Pandya.
- **SRH:** Nice Pattern of Acceleration, can take more risks in the first 6.
- **KKR:** Need to look into death over run rates. Excellent template till that point.
- **RCB:** Pathetic show in all the 3 phases. Too many wickets lost in PP, lack of runs.
- **GL:** A batting powerhouse. Finishing could be improved. 
  - **RPS:** The runners-up could breathe a bit easy by scoring some more runs in first 2 phases. Their middle phase of consolidation is uninspiring.
  - **GL:** The worst performing team with ball in hand. Neither do they pick up wickets, nor do they stem the flow of runs. Despite being one of the best batting teams, they suffer.
  - **RPS:** They make up for their batting shortcomings by bowling very well. So the success formula is to stem the flow of runs and consequentially pick up wickets.
  - **RCB:** A classic case. Whatever matches they won in IPL-2017 were batting first. They are not outstanding batting first, but they do a decent job. Batting second, they seem to fall off a cliff. No wonder their chases are unsuccessful. Their bowling performances run in parallel. They bowl well defending a target and suffer while bowling first.
  - **GL:** Their case contrasts that of RCB. They are a great bat-second team. In the first innings they need to accumulate more in the final flourish. Bowling needs to be improved, especially while defending a total.
  - **KXiP & DC:** Both do a pretty decent job, but their bowling standards should improve.
  - Good top-3, good finishers, along with a consolidator constitute a reasonable batting team.
  - The finest teams have at least one: good opening bowler, a good spinner to choke runs in the middle and a good death bowler to control the bludgeoning at the end.
