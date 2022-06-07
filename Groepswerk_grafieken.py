import pandas as pd
from SQL_functions import get_pandas
import matplotlib.pyplot as plt
import numpy as np


image_path = "Front_End/static/image"

city1 = 'paris'
city2 = 'naples'

# Get all data out of the SQL database for both cities
city1 = get_pandas(city1)
city2 = get_pandas(city2)
# print(city2.to_string())

# Get city name from each city
city_name1 = city1.iloc[0,0]
city_name2 = city2.iloc[0,0]

# Create plots for climate data
specs = ["TEMP_MIN", "TEMP_MAX", "RAIN", "RAINDAYS", "SUN"]
for spec in specs:
    # Get pandas subset with months and minimum temperature
    spec_pd1 = city1[city1["spec"] == spec]
    spec_pd2 = city2[city2["spec"] == spec]
    # Get index (months) and values
    index1 = spec_pd1["month"]
    index2 = spec_pd2["month"]
    value1 = spec_pd1["value"].astype(int)
    value2 = spec_pd2["value"].astype(int)
    # Get long description of spec
    title = spec_pd1.iloc[0,4]
    # Get description of measure
    measure = spec_pd1.iloc[0,5]

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(index1, value1, label=city_name1)
    ax.plot(index2, value2, label=city_name2)
    ax.set_xlabel("Months")
    ax.set_ylabel(measure)
    ax.set_title(title)
    ax.legend()

    fig.set_size_inches([6,5])
    fig.savefig(f"{image_path}/graph_{spec}.png", dpi=300)


# Create bar charts for the rest of the data
def create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure):
    x = np.arange(len(Specs))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, city1_values, width, label=city_name1, color='#301ee3')
    rects2 = ax.bar(x + width / 2, city2_values, width, label=city_name2, color='#b0f68e')
    ax.set_ylabel(measure)
    ax.set_title(title)
    if title != 'Crime':
        ax.set_xticks(x, Specs)
    else:
        # ax.set_xticklabels(Specs, rotation=25)
        ax.set_xticks(x, Specs, rotation=13)
    ax.legend()
    fig.set_size_inches([6, 5])
    fig.savefig(f"{image_path}/bar_{title}.png", dpi=300)

# Set spec as index
city1.set_index('spec', inplace=True)
city2.set_index('spec', inplace=True)

# Create a subset for 'a night out'
title = "A Night Out"
city1_data = city1.loc["LUNCH":"BEER", :]
city2_data = city2.loc["LUNCH":"BEER", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'Rent'
title = "Rent"
city1_data = city1.loc["EXPENSIVE FLAT":"NORMAL STUDIO", :]
city2_data = city2.loc["EXPENSIVE FLAT":"NORMAL STUDIO", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'Household'
title = "Household"
city1_data = city1.loc["UTILITIES":"CLEANING", :]
city2_data = city2.loc["UTILITIES":"CLEANING", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'Transport'
title = "Transport"
city1_data = city1.loc["GAS":"PUBLIC TRANSPORT", :]
city2_data = city2.loc["GAS":"PUBLIC TRANSPORT", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'clothing' items
title = "Clothes"
city1_data = city1.loc["JEANS":"SHOES", :]
city2_data = city2.loc["JEANS":"SHOES", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'shopping' items
title = "Shopping"
city1_data = city1.loc["CHICKEN":"COLA", :]
city2_data = city2.loc["CHICKEN":"COLA", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'safety' items
title = "Crime"
city1_data = city1.loc["CRIME":"DRUGS", :]
city2_data = city2.loc["CRIME":"DRUGS", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'pollution' items
title = "Pollution"
city1_data = city1.loc["POLLUTION":"NOISE", :]
city2_data = city2.loc["POLLUTION":"NOISE", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )

# Create a subset for 'city comfort' items
title = "City Comfort"
city1_data = city1.loc[["WALK_DAY", "WALK_NIGHT", "PARKS", "COMFORT"], :]
city2_data = city2.loc[["WALK_DAY", "WALK_NIGHT", "PARKS", "COMFORT"], :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
measure = city1_data.iloc[0,4]
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title, measure )


#
# output     print(city1.to_string())
#      city            spec  value month                                                                  description                            measure
# 0   perth        TEMP_MIN     18   JAN                                                          Minimum Temperature  degrees Celcius average per month
# 1   perth        TEMP_MAX     32   JAN                                                          Maximum Temperature  degrees Celcius average per month
# 2   perth            RAIN     15   JAN                                                                Precipitation              millimeters per month
# 3   perth        RAINDAYS      1   JAN                                                                   Rainy days                     days per month
# 4   perth        TEMP_MIN     18   FEB                                                          Minimum Temperature  degrees Celcius average per month
# 5   perth        TEMP_MAX     32   FEB                                                          Maximum Temperature  degrees Celcius average per month
# 6   perth            RAIN     15   FEB                                                                Precipitation              millimeters per month
# 7   perth        RAINDAYS      1   FEB                                                                   Rainy days                     days per month
# 8   perth        TEMP_MIN     16   MAR                                                          Minimum Temperature  degrees Celcius average per month
# 9   perth        TEMP_MAX     30   MAR                                                          Maximum Temperature  degrees Celcius average per month
# 10  perth            RAIN     20   MAR                                                                Precipitation              millimeters per month
# 11  perth        RAINDAYS      2   MAR                                                                   Rainy days                     days per month
# 12  perth        TEMP_MIN     14   APR                                                          Minimum Temperature  degrees Celcius average per month
# 13  perth        TEMP_MAX     26   APR                                                          Maximum Temperature  degrees Celcius average per month
# 14  perth            RAIN     30   APR                                                                Precipitation              millimeters per month
# 15  perth        RAINDAYS      4   APR                                                                   Rainy days                     days per month
# 16  perth        TEMP_MIN     11   MAY                                                          Minimum Temperature  degrees Celcius average per month
# 17  perth        TEMP_MAX     22   MAY                                                          Maximum Temperature  degrees Celcius average per month
# 18  perth            RAIN     80   MAY                                                                Precipitation              millimeters per month
# 19  perth        RAINDAYS      9   MAY                                                                   Rainy days                     days per month
# 20  perth        TEMP_MIN      9   JUN                                                          Minimum Temperature  degrees Celcius average per month
# 21  perth        TEMP_MAX     20   JUN                                                          Maximum Temperature  degrees Celcius average per month
# 22  perth            RAIN    125   JUN                                                                Precipitation              millimeters per month
# 23  perth        RAINDAYS     12   JUN                                                                   Rainy days                     days per month
# 24  perth        TEMP_MIN      8   JUL                                                          Minimum Temperature  degrees Celcius average per month
# 25  perth        TEMP_MAX     18   JUL                                                          Maximum Temperature  degrees Celcius average per month
# 26  perth            RAIN    140   JUL                                                                Precipitation              millimeters per month
# 27  perth        RAINDAYS     14   JUL                                                                   Rainy days                     days per month
# 28  perth        TEMP_MIN      8   AUG                                                          Minimum Temperature  degrees Celcius average per month
# 29  perth        TEMP_MAX     19   AUG                                                          Maximum Temperature  degrees Celcius average per month
# 30  perth            RAIN    120   AUG                                                                Precipitation              millimeters per month
# 31  perth        RAINDAYS     13   AUG                                                                   Rainy days                     days per month
# 32  perth        TEMP_MIN      9   SEP                                                          Minimum Temperature  degrees Celcius average per month
# 33  perth        TEMP_MAX     21   SEP                                                          Maximum Temperature  degrees Celcius average per month
# 34  perth            RAIN     80   SEP                                                                Precipitation              millimeters per month
# 35  perth        RAINDAYS     11   SEP                                                                   Rainy days                     days per month
# 36  perth        TEMP_MIN     11   OCT                                                          Minimum Temperature  degrees Celcius average per month
# 37  perth        TEMP_MAX     24   OCT                                                          Maximum Temperature  degrees Celcius average per month
# 38  perth            RAIN     35   OCT                                                                Precipitation              millimeters per month
# 39  perth        RAINDAYS      5   OCT                                                                   Rainy days                     days per month
# 40  perth        TEMP_MIN     13   NOV                                                          Minimum Temperature  degrees Celcius average per month
# 41  perth        TEMP_MAX     27   NOV                                                          Maximum Temperature  degrees Celcius average per month
# 42  perth            RAIN     30   NOV                                                                Precipitation              millimeters per month
# 43  perth        RAINDAYS      4   NOV                                                                   Rainy days                     days per month
# 44  perth        TEMP_MIN     16   DEC                                                          Minimum Temperature  degrees Celcius average per month
# 45  perth        TEMP_MAX     30   DEC                                                          Maximum Temperature  degrees Celcius average per month
# 46  perth            RAIN     10   DEC                                                                Precipitation              millimeters per month
# 47  perth        RAINDAYS      2   DEC                                                                   Rainy days                    hours per month
# 48  perth             SUN    355   JAN                                                                   Sunny days                    hours per month
# 49  perth             SUN    320   FEB                                                                   Sunny days                    hours per month
# 50  perth             SUN    300   MAR                                                                   Sunny days                    hours per month
# 51  perth             SUN    250   APR                                                                   Sunny days                    hours per month
# 52  perth             SUN    205   MAY                                                                   Sunny days                    hours per month
# 53  perth             SUN    175   JUN                                                                   Sunny days                    hours per month
# 54  perth             SUN    190   JUL                                                                   Sunny days                    hours per month
# 55  perth             SUN    225   AUG                                                                   Sunny days                    hours per month
# 56  perth             SUN    230   SEP                                                                   Sunny days                    hours per month
# 57  perth             SUN    300   OCT                                                                   Sunny days                    hours per month
# 58  perth             SUN    320   NOV                                                                   Sunny days                    hours per month
# 59  perth             SUN    355   DEC                                                                   Sunny days                    hours per month
# 60  perth           LUNCH     15    NA            Basic lunchtime menu (including a drink) in the business district                                USD
# 61  perth          MOVIES     25    NA                                                      2 tickets to the movies                                USD
# 62  perth            BEER      7    NA                                 1 beer in neighbourhood pub (500ml or 1pt.)                                 USD
# 63  perth        FLAT_EXP   1444    NA  Monthly rent for 85 m2 (900 sqft) furnished accommodation in expensive area                                USD
# 64  perth       FLAT_NORM   1166    NA     Monthly rent for 85 m2 (900 sqft) furnished accommodation in normal area                                USD
# 65  perth      STUDIO_EXP   1271    NA       Monthly rent for a 45 m2 (480 sqft) furnished studio in expensive area                                USD
# 66  perth     STUDIO_NORM    867    NA         Monthly rent for a 45 m2 (480 sqft) furnished studio in normal area                                 USD
# 67  perth       UTILITIES    262    NA  Utilities 1 month (heating, electricity, gas ...) for 2 people in 85m2 flat                                USD
# 68  perth       MICROWAVE    153    NA   Microwave 800/900 watt (bosch, panasonic, lg, sharp, or equivalent brands)                                USD
# 69  perth        CLEANING  176.0    NA                                                     8 hours of cleaning help                                USD
# 70  perth             GAS   61.5    NA                                               1 full tank of gas (50 liters)                                USD
# 71  perth       TRANSPORT    116    NA                                              Monthly ticket public transport                                USD
# 72  perth           JEANS     63    NA                                       1 pair of jeans (levis 501 or similar)                                USD
# 73  perth           SHOES    108    NA                   1 pair of sport shoes (nike, adidas, or equivalent brands)                                USD
# 74  perth         CHICKEN   3.96    NA                                    500 gr (1 lb.) of boneless chicken breast                                USD
# 75  perth            WINE     11    NA                                     1 bottle of red table wine, good quality                                USD
# 76  perth            COLA   1.94    NA                                                        2 liters of coca-cola                                USD
# 77  perth           CRIME  43.99    NA                                                               Level of crime                        Scale 1-100
# 78  perth     HOME_BROKEN  42.13    NA                                        Worries home broken and things stolen                        Scale 1-100
# 79  perth   MUGGED_ROBBED  33.66    NA                                               Worries being mugged or robbed                        Scale 1-100
# 80  perth      CAR_STOLEN  30.39    NA                                                           Worries car stolen                        Scale 1-100
# 81  perth        ATTACKED  40.14    NA                                                       Worries being attacked                        Scale 1-100
# 82  perth           DRUGS  55.04    NA                                        Problem people using or dealing drugs                        Scale 1-100
# 83  perth        WALK_DAY  76.35    NA                                         Safety walking alone during daylight                        Scale 1-100
# 84  perth      WALK_NIGHT  43.04    NA                                            Safety walking alone during night                        Scale 1-100
# 85  perth       POLLUTION  23.14    NA                                                              Pollution Index                        Scale 1-100
# 86  perth             AIR  17.06    NA                                                                Air Pollution                        Scale 1-100
# 87  perth  DRINKING_WATER  13.94    NA                                 Drinking Water Pollution and Inaccessibility                        Scale 1-100
# 88  perth            DIRT  26.29    NA                                                             Dirty and Untidy                        Scale 1-100
# 89  perth           NOISE  31.79    NA                                                    Noise and Light Pollution                        Scale 1-100
# 90  perth         COMFORT  82.04    NA                                        Comfortable to Spend Time in the City                        Scale 1-100
# 91  perth           PARKS  83.10    NA                                                   Quality of Green and Parks                        Scale 1-100
