# DS2000-Project-2-Stock-Market-Data-Analysis-and-Visualisation
Course work of "DS2000 Programming with Data" that builds a single-index model for stocks price changes to evaluate the stocks' risk.

# Background and Motivation
I would like to build a single-index model for stocks price changes to evaluate the stocks' risk. The financial concept "high risk high return" means that the investors will be compensated for bearing high risk by higher return. However, some risks are firm specific risk that can be eliminated through portfolio diversification. Investors will only be compensated for the risk they bear that can not be eliminated by diversification, which is the systematic risk(also called market risk).
Basically, the project is running a regression of the return of stocks against the market return(approximated by S&P500) to find the correlation coefficient of a certain stock's return and the market changes. The correlation coefficient represents the systematic risk of the stock. By generating graphs of regression, one can judge the market risk from the slopes.

# Something Special
This project is originally the course work of "DS2000 Programming with Data" which is my first programming course ever. I met some problems in the data visualization part at that time. I wanted to fix the problem with my improved python skills when I display them on GitHub. Then, I found that the way I used to store data using dictionaries is not efficient, and the data structure is hard to understand. So, I re-write the entire code with pandas to make it more clear. The revised version of work is integrated into the jupyter notebook file, and the original copy of course work is also uploaded (python code with a pdf form report) for comparison.
