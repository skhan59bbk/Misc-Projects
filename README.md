# Misc-Projects
A place to store miscellaneous projects I have been playing around with.


## Mortgage Overpayment
* What: Very quick and dirty visualisation of the effect on the life of my mortgage by overpaying each month.
* Libraries: numpy, matplotlib
* Takeaways: Making use of list comprehension and toying with matplotlib.pyplot basics

## London Happiness
* What: Quantitative responses to various measures of happiness across London's boroughs
* Libraries: pandas, matplotlib
* Takeaways: Transforming original data into something more usable for this particular visualisation objective.

## Takeover Panel Disclosures
* What: The Panel of Takeovers and Mergers is a UK body that publishes a daily list of companies targeted for takeover (and the respective offering company). The format of the daily data is a semi-structured .csv file that must be reshaped in order to extract anything of value from the file. e Python file in this repository does just that. After downloading the file, the key elements are extracted for each takeover deal, including the offeree and offeror names and identifiers, plus whether or not a regulatory disclosure is required for the offeror company. In practice, this can then be loaded into a database (for example) and then used to compare against a portfolio to determine whether there are any regulatory obligations required.
* Libraries: pandas, os
* Takeaways: Transforming data from semi-structured to structured for further analysis (e.g. loading into SQL database).

