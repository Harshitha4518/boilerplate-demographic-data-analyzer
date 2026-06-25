import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    higher_ed = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_ed_rich = round((df[higher_ed & (df['salary'] == '>50K')].shape[0] / df[higher_ed].shape[0]) * 100, 1)
    lower_ed_rich = round((df[~higher_ed & (df['salary'] == '>50K')].shape[0] / df[~higher_ed].shape[0]) * 100, 1)

    min_work_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_ed_rich)
        print("Percentage without higher education that earn >50K:", lower_ed_rich)
        print("Min work time:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage)
        print("Country with highest % earning >50K:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupation in India for >50K earners:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_ed_rich,
        'lower_education_rich': lower_ed_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
