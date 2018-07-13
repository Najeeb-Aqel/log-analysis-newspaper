# Movie_Project

analysis-project is a reprting tool that is designed to deal with big data and millions of entries
to extract bussiness conclusions and isights from raw data to help businesses grow and make the right decisions.

# Prerequisites

Python 2.7 or hiher: You can download it from the official site - [Python Software Foundation](https://www.python.org)



# Installation 


1. clone the project to your computer: ` git clone https://github.com/najeebael/Movie_Project `

2. In the command line change directory: ` ~/vagrant `

3. Run vagrant virtual machine: ` vagrant up `

4. create the following tables:
      * `select date(time) as fordate, count(*) as num into logTotal  from log  group by date(time) order by fordate;`
      * `select date(time) as fordate, count(*) as num into logbad from log where log.status='404 NOT FOUND' group by date(time) order by fordate;`
      * `select logTotal.fordate,((logbad.num* 1.00) / logTotal.num) * 100 as perc into percentageB from logTotal,logbad where logTotal.fordate=logbad.fordate group by perc,logTotal.fordate;`

4. Run main.py: ` python main.py `

# Built With

* [Vagrant](https://www.virtualbox.org/wiki/Downloads)
* [Virtualbox](https://www.vagrantup.com/)

# References

* [UdacityCourse](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/ffdd3161-2adb-4592-af11-62109c110ffd)
* [SQL Count](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
* [Concatenation in sql](https://stackoverflow.com/questions/3828842/how-to-like-two-columns-in-one-sql-statement)
* [operations in sql](https://social.msdn.microsoft.com/Forums/sqlserver/en-US/d833b7bc-4909-473f-bfd7-9a53ea0ef8c3/evaluate-percentage-using-two-columns-of-a-table?forum=transactsql)



