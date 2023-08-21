import pandas as pd
from persiantools.jdatetime import JalaliDate
import datetime
from hijri_converter import convert

# create a list of dates
dates = pd.date_range(start='2022-01-01', end='2022-01-31')

# create empty lists for each date column
iranian_dates = []
national_dates = []
arab_dates = []

# loop through each date and convert to Iranian, National, and Arab date formats
for date in dates:
    # convert to Jalali (Iranian) date
    iranian = JalaliDate.to_jalali(date.date())
    iranian_date = f"{iranian.year}/{iranian.month}/{iranian.day}"
    iranian_dates.append(iranian_date)

    # convert to National date
    national_date = date.strftime('%Y/%m/%d')
    national_dates.append(national_date)

    # convert to Hijri (Arab) date
    arab_date = convert(date.strftime('%Y-%m-%d')).strftime('%Y/%m/%d')
    arab_dates.append(arab_date)

# create a pandas dataframe with the date columns
df = pd.DataFrame({'Iranian Date': iranian_dates,
                   'National Date': national_dates,
                   'Arab Date': arab_dates})

# create a Pandas Excel writer using xlsxwriter engine
writer = pd.ExcelWriter('dates.xlsx', engine='xlsxwriter')

# write the dataframe to the Excel file
df.to_excel(writer, index=False)

# save the Excel file and close the Pandas Excel writer
writer.save()






