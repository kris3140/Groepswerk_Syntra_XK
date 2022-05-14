import pandas as pd
from SQL_functions import get_pandas
import matplotlib.pyplot as plt
import numpy as np


# Get all data out of the SQL database for both cities
city1 = get_pandas(61)
city2 = get_pandas(55)

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
    fig.savefig(f"graph_{spec}.png", dpi=300)


# Create bar charts for the rest of the data
def create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title ):
    x = np.arange(len(Specs))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, city1_values, width, label=city_name1, color='#301ee3')
    rects2 = ax.bar(x + width / 2, city2_values, width, label=city_name2, color='#b0f68e')
    ax.set_ylabel('USD')
    ax.set_title(title)
    ax.set_xticks(x, Specs)
    ax.legend()
    fig.set_size_inches([6, 5])
    fig.savefig(f"bar_{title}.png", dpi=300)

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
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'Rent'
title = "Rent"
city1_data = city1.loc["RENT1":"RENT4", :]
city2_data = city2.loc["RENT1":"RENT4", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'Household'
title = "Household"
city1_data = city1.loc["UTILITIES":"CLEANING", :]
city2_data = city2.loc["UTILITIES":"CLEANING", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'Transport'
title = "Transport"
city1_data = city1.loc["GAS":"TRANSPORT", :]
city2_data = city2.loc["GAS":"TRANSPORT", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'clothing' items
title = "Clothing"
city1_data = city1.loc["JEANS":"SHOES", :]
city2_data = city2.loc["JEANS":"SHOES", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'shopping' items
title = "Shopping"
city1_data = city1.loc["CHICKEN":"COLA", :]
city2_data = city2.loc["CHICKEN":"COLA", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'safety' items
title = "Safety"
city1_data = city1.loc["CRIME":"DRUGS", :]
city2_data = city2.loc["CRIME":"DRUGS", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'poluttion' items
title = "Poluttion"
city1_data = city1.loc["POLLUTION":"NOISE", :]
city2_data = city2.loc["POLLUTION":"NOISE", :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )

# Create a subset for 'city comfort' items
title = "City Comfort"
city1_data = city1.loc[["WALK_DAY", "WALK_NIGHT", "PARKS", "COMFORT"], :]
city2_data = city2.loc[["WALK_DAY", "WALK_NIGHT", "PARKS", "COMFORT"], :]
city1_values = list(city1_data["value"].astype(float))
city2_values = list(city2_data["value"].astype(float))
Specs = city1_data.index
create_barchart(Specs, city1_values, city2_values, city_name1, city_name2, title )


#
# output     print(city1.to_string())
#         city            spec  value month                                                                  description                            measure
# 0   brussels        TEMP_MIN      1   JAN                                                          Minimum Temperature  degrees Celcius average per month
# 1   brussels        TEMP_MAX      6   JAN                                                          Maximum Temperature  degrees Celcius average per month
# 2   brussels            RAIN     75   JAN                                                                     Rainfall              millimeters per month
# 3   brussels        RAINDAYS     13   JAN                                                                   Rainy Days                     days per month
# 4   brussels        TEMP_MIN      1   FEB                                                          Minimum Temperature  degrees Celcius average per month
# 5   brussels        TEMP_MAX      7   FEB                                                          Maximum Temperature  degrees Celcius average per month
# 6   brussels            RAIN     65   FEB                                                                     Rainfall              millimeters per month
# 7   brussels        RAINDAYS     12   FEB                                                                   Rainy Days                     days per month
# 8   brussels        TEMP_MIN      3   MAR                                                          Minimum Temperature  degrees Celcius average per month
# 9   brussels        TEMP_MAX     11   MAR                                                          Maximum Temperature  degrees Celcius average per month
# 10  brussels            RAIN     60   MAR                                                                     Rainfall              millimeters per month
# 11  brussels        RAINDAYS     11   MAR                                                                   Rainy Days                     days per month
# 12  brussels        TEMP_MIN      5   APR                                                          Minimum Temperature  degrees Celcius average per month
# 13  brussels        TEMP_MAX     15   APR                                                          Maximum Temperature  degrees Celcius average per month
# 14  brussels            RAIN     45   APR                                                                     Rainfall              millimeters per month
# 15  brussels        RAINDAYS      9   APR                                                                   Rainy Days                     days per month
# 16  brussels        TEMP_MIN      8   MAY                                                          Minimum Temperature  degrees Celcius average per month
# 17  brussels        TEMP_MAX     18   MAY                                                          Maximum Temperature  degrees Celcius average per month
# 18  brussels            RAIN     65   MAY                                                                     Rainfall              millimeters per month
# 19  brussels        RAINDAYS     10   MAY                                                                   Rainy Days                     days per month
# 20  brussels        TEMP_MIN     11   JUN                                                          Minimum Temperature  degrees Celcius average per month
# 21  brussels        TEMP_MAX     21   JUN                                                          Maximum Temperature  degrees Celcius average per month
# 22  brussels            RAIN     65   JUN                                                                     Rainfall              millimeters per month
# 23  brussels        RAINDAYS     10   JUN                                                                   Rainy Days                     days per month
# 24  brussels        TEMP_MIN     13   JUL                                                          Minimum Temperature  degrees Celcius average per month
# 25  brussels        TEMP_MAX     24   JUL                                                          Maximum Temperature  degrees Celcius average per month
# 26  brussels            RAIN     80   JUL                                                                     Rainfall              millimeters per month
# 27  brussels        RAINDAYS     10   JUL                                                                   Rainy Days                     days per month
# 28  brussels        TEMP_MIN     13   AUG                                                          Minimum Temperature  degrees Celcius average per month
# 29  brussels        TEMP_MAX     23   AUG                                                          Maximum Temperature  degrees Celcius average per month
# 30  brussels            RAIN     90   AUG                                                                     Rainfall              millimeters per month
# 31  brussels        RAINDAYS     10   AUG                                                                   Rainy Days                     days per month
# 32  brussels        TEMP_MIN     11   SEP                                                          Minimum Temperature  degrees Celcius average per month
# 33  brussels        TEMP_MAX     20   SEP                                                          Maximum Temperature  degrees Celcius average per month
# 34  brussels            RAIN     60   SEP                                                                     Rainfall              millimeters per month
# 35  brussels        RAINDAYS     10   SEP                                                                   Rainy Days                     days per month
# 36  brussels        TEMP_MIN      8   OCT                                                          Minimum Temperature  degrees Celcius average per month
# 37  brussels        TEMP_MAX     15   OCT                                                          Maximum Temperature  degrees Celcius average per month
# 38  brussels            RAIN     65   OCT                                                                     Rainfall              millimeters per month
# 39  brussels        RAINDAYS     10   OCT                                                                   Rainy Days                     days per month
# 40  brussels        TEMP_MIN      4   NOV                                                          Minimum Temperature  degrees Celcius average per month
# 41  brussels        TEMP_MAX     10   NOV                                                          Maximum Temperature  degrees Celcius average per month
# 42  brussels            RAIN     75   NOV                                                                     Rainfall              millimeters per month
# 43  brussels        RAINDAYS     12   NOV                                                                   Rainy Days                     days per month
# 44  brussels        TEMP_MIN      2   DEC                                                          Minimum Temperature  degrees Celcius average per month
# 45  brussels        TEMP_MAX      7   DEC                                                          Maximum Temperature  degrees Celcius average per month
# 46  brussels            RAIN     85   DEC                                                                     Rainfall              millimeters per month
# 47  brussels        RAINDAYS     13   DEC                                                                   Rainy Days                     days per month
# 48  brussels             SUN     60   JAN                                                                     Sunshine                    hours per month
# 49  brussels             SUN     75   FEB                                                                     Sunshine                    hours per month
# 50  brussels             SUN    120   MAR                                                                     Sunshine                    hours per month
# 51  brussels             SUN    170   APR                                                                     Sunshine                    hours per month
# 52  brussels             SUN    200   MAY                                                                     Sunshine                    hours per month
# 53  brussels             SUN    190   JUN                                                                     Sunshine                    hours per month
# 54  brussels             SUN    205   JUL                                                                     Sunshine                    hours per month
# 55  brussels             SUN    195   AUG                                                                     Sunshine                    hours per month
# 56  brussels             SUN    145   SEP                                                                     Sunshine                    hours per month
# 57  brussels             SUN    120   OCT                                                                     Sunshine                    hours per month
# 58  brussels             SUN     65   NOV                                                                     Sunshine                    hours per month
# 59  brussels             SUN     45   DEC                                                                     Sunshine                    hours per month
# 60  brussels           LUNCH     16    NA            Basic lunchtime menu (including a drink) in the business district                                USD
# 61  brussels          MOVIES     25    NA                                                      2 tickets to the movies                                USD
# 62  brussels            BEER   4.13    NA                                 1 beer in neighbourhood pub (500ml or 1pt.)                                 USD
# 63  brussels            RENT   1049    NA     Monthly rent for 85 m2 (900 sqft) furnished accommodation in normal area                                USD
# 64  brussels       UTILITIES    129    NA  Utilities 1 month (heating, electricity, gas ...) for 2 people in 85m2 flat                                USD
# 65  brussels       MICROWAVE    169    NA   Microwave 800/900 watt (bosch, panasonic, lg, sharp, or equivalent brands)                                USD
# 66  brussels        CLEANING     11    NA                                                Hourly rate for cleaning help                                USD
# 67  brussels             GAS   1.59    NA                                                  1 liter (1/4 gallon) of gas                                USD
# 68  brussels       TRANSPORT     53    NA                                              Monthly ticket public transport                                USD
# 69  brussels           JEANS     90    NA                                       1 pair of jeans (levis 501 or similar)                                USD
# 70  brussels           SHOES     89    NA                   1 pair of sport shoes (nike, adidas, or equivalent brands)                                USD
# 71  brussels         CHICKEN   4.88    NA                                    500 gr (1 lb.) of boneless chicken breast                                USD
# 72  brussels            WINE      9    NA                                     1 bottle of red table wine, good quality                                USD
# 73  brussels            COLA   2.63    NA                                                        2 liters of coca-cola                                USD
# 74  brussels           CRIME  57.12    NA                                                               Level of crime                        Scale 1-100
# 75  brussels     HOME_BROKEN  49.56    NA                                        Worries home broken and things stolen                        Scale 1-100
# 76  brussels   MUGGED_ROBBED  53.37    NA                                               Worries being mugged or robbed                        Scale 1-100
# 77  brussels      CAR_STOLEN  41.44    NA                                                           Worries car stolen                        Scale 1-100
# 78  brussels        ATTACKED  53.80    NA                                                       Worries being attacked                        Scale 1-100
# 79  brussels        INSULTED  55.57    NA                                                       Worries being insulted                        Scale 1-100
# 80  brussels           DRUGS  56.99    NA                                        Problem people using or dealing drugs                        Scale 1-100
# 81  brussels        WALK_DAY  67.09    NA                                         Safety walking alone during daylight                        Scale 1-100
# 82  brussels      WALK_NIGHT  36.95    NA                                            Safety walking alone during night                        Scale 1-100
# 83  brussels       POLLUTION  62.00    NA                                                              Pollution Index                        Scale 1-100
# 84  brussels             AIR  64.06    NA                                                                Air Pollution                        Scale 1-100
# 85  brussels  DRINKING_WATER  34.86    NA                                 Drinking Water Pollution and Inaccessibility                        Scale 1-100
# 86  brussels            DIRT  62.73    NA                                                             Dirty and Untidy                        Scale 1-100
# 87  brussels           NOISE  54.86    NA                                                    Noise and Light Pollution                        Scale 1-100
# 88  brussels           WATER  44.58    NA                                                              Water Pollution                        Scale 1-100
# 89  brussels         COMFORT  54.82    NA                                        Comfortable to Spend Time in the City                        Scale 1-100
# 90  brussels           PARKS  69.91    NA                                                   Quality of Green and Parks                        Scale 1-100
