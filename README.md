# Task 3 - Exploratory Data Analysis (EDA)

## Problem Statement
Netflix has thousands of shows. We want to explore this data to find patterns. Which countries produce most content? What ratings are common? How are IMDB scores distributed? EDA helps us answer these questions using statistics and charts.

---

## Dataset Details

 Field          |            Details                      
--------------|------------------------------
 Dataset Name | Netflix Shows Dataset        
 Total Rows   | 15 shows                     
 Total Columns| 7 columns                    
 Source       | Defined inside the code      

 Column Name  | Description                              
--------------|------------------------------------------
 title        | Name of the show                         
 type         | Movie or TV Show                         
 country      | Country where it was produced            
 release_year | Year the show was released               
 rating       | Age rating like TV-MA TV-14 etc          
 seasons      | Number of seasons                        
 imdb_score   | IMDB rating out of 10                    

---

## Approach

Step 1 - Define Netflix data as dictionary and create DataFrame

Step 2 - Print summary statistics using describe()

Step 3 - Print correlation between numeric columns

Step 4 - Count shows by release year to see trend

Step 5 - Create Bar Chart for shows by country

Step 6 - Create Bar Chart for rating distribution

Step 7 - Create Histogram for IMDB score distribution

Step 8 - Create Scatter Plot for release year vs IMDB score

---

## Results

 Analysis     |            Finding 
--------------------------------------------------------------------
 Top Country  | United States has most shows                         
 Top Rating   | TV-MA is most common rating                          
 IMDB Average | Most shows score between 8.0 and 8.8  

 Metric       | Value                        
------------------------------------------
 Total Shows  | 15                           
 Countries    | 6 different countries        
 IMDB Range   | 6.9 to 8.8                   
 Chart saved  | task3_output.png             
