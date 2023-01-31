import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df = pd.read_csv("adult.data.csv")
    races = df["race"].unique()
    count_races= df["race"].value_counts()
    race_count = pd.Series(count_races,index=races)

    
    
    # What is the average age of men?
    age_count = df[df["sex"]=="Male"]
    average_age_men = round(age_count["age"].sum()/len(age_count),1)
    
    # What is the percentage of people who have a Bachelor's degree?
    bachelor_count = df[df["education"] == "Bachelors"]
    percentage_bachelors = round((len(bachelor_count)/len(df))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
     # percentage with salary >50K
    education =["Bachelors","Master","Doctorate"] 
    higher_education_count = df[df["education"].isin(education)]
    higher_education_rich = round((len(higher_education_count[higher_education_count["salary"] == ">50K"])/len(higher_education_count)*100),1)
    lower_education_count = df[~df["education"].isin(education)]
    lower_education_rich = round((len(lower_education_count[lower_education_count["salary"] == ">50K"])/len(lower_education_count))*100,1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    h_p_w = df["hours-per-week"].value_counts()
    min_work_hours = h_p_w.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(len(num_min_workers[num_min_workers["salary"] == ">50K"])/(len(num_min_workers))*100,1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df[df["salary"] == ">50K"]
    country = highest_earning_country["native-country"].value_counts()
    country1 = df["native-country"].value_counts()
    country = country/country1
    country = country[country == country.max()]
    highest_earning_country = country.index[0]
    highest_earning_country_percentage = round(country.values[0]*100,1)



    # Identify the most popular occupation for those who earn >50K in India.
    india = df[df["native-country"] == "India"]
    india_high_earners = india[india["salary"] == ">50K"]
    popular_job = india_high_earners["occupation"].value_counts()
    max = popular_job.max()
    top_IN_occupation = popular_job[popular_job == max].index[0]
   
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

