# student_grades
Requirements met 

* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program

* Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

* Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display

* streathing my knowledge using basic machine learning to predict outcomes 

this program takes a CSV file with student test results with different variables from the CSV that I selected from the document and runs a regression. 
First I turned one of the variables into an interger in order for me to be able to use it in a regression. Then placed the variable turned integer into a 
new column in the CSV file. 
After that created variables that will hold the data for the x and y axis and ran a regression. T
he next step was testing the variables using only a small portion of the data.
and find the accuracy of the prediction. That can be found if you print the accuracy variable. 
The last step was getting the program to predict the test scores of the remaining student data.


Just run the program and it will print out the predictions made compared to the actually test score. 
I.E. 14.24946948240673 [15 14  6  3  0  0] 14 ( the number with decimal (14.2499) is the prediction and the far right out of the bracket number (14)is the actual score)
