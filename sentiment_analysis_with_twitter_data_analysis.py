import matplotlib.pyplot as plt
import pandas as pd

# load the rest of the "standard" set of packages
import numpy as np
# import statsmodels.api as sm
# import matplotlib.pyplot as plt

# Overall objective: “Which next-gen gaming console should I acquire – 
# the PlayStation 5 or the Xbox Series X?”  
# (this objective might end up changing over time depending on circumstances)

# Identify file names for data import

firstTwitterSearchResult = 'results_PlayStation 5_2021-01-06_13,12,31_EasternStandardTime.csv'
secondTwitterSearchResult = 'results_Xbox Series X_2021-01-06_13,12,34_EasternStandardTime.csv'

# Import data from files

twitter_data_PS5 = pd.read_csv(firstTwitterSearchResult)
twitter_data_Series_X = pd.read_csv(secondTwitterSearchResult)

# Isolate polarity data for both the PS5 and the Series X
PS5_polarity_data = twitter_data_PS5.polarity
Series_X_polarity_data = twitter_data_Series_X.polarity

# Acquire 5-number summary and mean for polarity scores for the PS5

PS5_polarity_Min = PS5_polarity_data.min()
PS5_polarity_LQ = np.percentile(PS5_polarity_data, 25)
PS5_polarity_Median = np.percentile(PS5_polarity_data, 50)
PS5_polarity_UQ = np.percentile(PS5_polarity_data, 75)
PS5_polarity_Max = PS5_polarity_data.max()

print("\n")

print("PS5 Polarity Min = " + str(PS5_polarity_Min))
print("PS5 Polarity Lower Quartile = " + str(PS5_polarity_LQ))
print("PS5 Polarity Median = " + str(PS5_polarity_Median))
print("PS5 Polarity Upper Quartile = " + str(PS5_polarity_UQ))
print("PS5 Polarity Max = " + str(PS5_polarity_Max))

# print("\n")

simple_mean_PS5_polarity = PS5_polarity_data.mean()
print("Simple mean for PS5 polarity scores: " + 
      str(round(simple_mean_PS5_polarity, 2)))

# Acquire the 5-number summary and mean for the polarity scores for the Series X

Series_X_polarity_Min = Series_X_polarity_data.min()
Series_X_polarity_LQ = np.percentile(Series_X_polarity_data, 25)
Series_X_polarity_Median = np.percentile(Series_X_polarity_data, 50)
Series_X_polarity_UQ = np.percentile(Series_X_polarity_data, 75)
Series_X_polarity_Max = Series_X_polarity_data.max()

print("\n")

print("Series X Polarity Min = " + str(Series_X_polarity_Min))
print("Series X Polarity Lower Quartile = " + str(Series_X_polarity_LQ))
print("Series X Polarity Median = " + str(Series_X_polarity_Median))
print("Series X Polarity Upper Quartile = " + str(Series_X_polarity_UQ))
print("Series X Polarity Max = " + str(Series_X_polarity_Max))

# print("\n")

simple_mean_Series_X_polarity = Series_X_polarity_data.mean()
print("Simple mean for Series X polarity scores: " + str(round(simple_mean_Series_X_polarity, 2)))

print("\n")

# Showcase box-and-whisker plot for polarity values of each console
PS5_polarity_data = twitter_data_PS5.polarity
Series_X_polarity_data = twitter_data_Series_X.polarity

plt.figure()
console_polarity_array = [PS5_polarity_data, Series_X_polarity_data]
plt.boxplot(console_polarity_array, 
            showmeans = True, 
            meanprops={"marker": "o", 
                       "markerfacecolor": "black", 
                       "markeredgecolor": "black"})
plt.title("Box-and-Whisker Plot: Next-Gen Polarity Values")
plt.xticks([1,2], ["PS5", "Series X"])
plt.xlabel("Next-Gen Console")
plt.ylabel("polarity")
plt.show()

# Acquire weighted 5-number summary and mean for polarity scores for the PS5
PS5_retweet_count_data = twitter_data_PS5.retwc

array_for_weighted_stats_PS5_polarity = np.repeat(PS5_polarity_data, 
                                                  PS5_retweet_count_data)
# print(array_for_weighted_stats_PS5_polarity)

# Acquire 5-number summary and mean for polarity scores for the PS5

PS5_polarity_weighted_Min = array_for_weighted_stats_PS5_polarity.min()
PS5_polarity_weighted_LQ = np.percentile(array_for_weighted_stats_PS5_polarity, 25)
PS5_polarity_weighted_Median = np.percentile(array_for_weighted_stats_PS5_polarity, 50)
PS5_polarity_weighted_UQ = np.percentile(array_for_weighted_stats_PS5_polarity, 75)
PS5_polarity_weighted_Max = array_for_weighted_stats_PS5_polarity.max()

print("\n")

print("PS5 Polarity Weighted Min = " + str(PS5_polarity_weighted_Min))
print("PS5 Polarity Weighted Lower Quartile = " + str(PS5_polarity_weighted_LQ))
print("PS5 Polarity Weighted Median = " + str(PS5_polarity_weighted_Median))
print("PS5 Polarity Weighted Upper Quartile = " + str(PS5_polarity_weighted_UQ))
print("PS5 Polarity Weighted Max = " + str(PS5_polarity_weighted_Max))

# print("\n")

weighted_mean_PS5_polarity = array_for_weighted_stats_PS5_polarity.mean()
print("Weighted mean for PS5 polarity scores: " + 
      str(round(weighted_mean_PS5_polarity, 2)))

# reference_weighted_mean_PS5_polarity = round(np.average(PS5_polarity_data, 
#                                               weights = PS5_retweet_count_data), 2)
# print("Reference Calculation of Weighted mean for PS5 polarity scores: " + 
#       str(round(reference_weighted_mean_PS5_polarity, 2)))

# Acquire weighted 5-number summary and mean for polarity scores for the Series X
Series_X_retweet_count_data = twitter_data_Series_X.retwc

array_for_weighted_stats_Series_X_polarity = np.repeat(Series_X_polarity_data, 
                                                  Series_X_retweet_count_data)

# print(array_for_weighted_stats_Series_X_polarity)

Series_X_polarity_weighted_Min = array_for_weighted_stats_Series_X_polarity.min()
Series_X_polarity_weighted_LQ = np.percentile(array_for_weighted_stats_Series_X_polarity, 25)
Series_X_polarity_weighted_Median = np.percentile(array_for_weighted_stats_Series_X_polarity, 50)
Series_X_polarity_weighted_UQ = np.percentile(array_for_weighted_stats_Series_X_polarity, 75)
Series_X_polarity_weighted_Max = array_for_weighted_stats_Series_X_polarity.max()

print("\n")

print("Series X Polarity Weighted Min = " + str(Series_X_polarity_weighted_Min))
print("Series X Polarity Weighted Lower Quartile = " + str(Series_X_polarity_weighted_LQ))
print("Series X Polarity Weighted Median = " + str(Series_X_polarity_weighted_Median))
print("Series X Polarity Weighted Upper Quartile = " + str(Series_X_polarity_weighted_UQ))
print("Series X Polarity Weighted Max = " + str(Series_X_polarity_weighted_Max))

# print("\n")

weighted_mean_Series_X_polarity = array_for_weighted_stats_Series_X_polarity.mean()
print("Weighted mean for Series X polarity scores: " + 
      str(round(weighted_mean_Series_X_polarity, 2)))

# reference_weighted_mean_Series_X_polarity = round(np.average(Series_X_polarity_data, 
#                                                              weights = Series_X_retweet_count_data), 2)
# print("Weighted mean for Series X polarity scores: " + 
#       str(round(reference_weighted_mean_Series_X_polarity, 2)))

print("\n")

# Showcase box-and-whisker plot for weighted polarity values of each console
PS5_weighted_polarity_data = array_for_weighted_stats_PS5_polarity
Series_X_weighted_polarity_data = array_for_weighted_stats_Series_X_polarity

plt.figure()
console_weighted_polarity_array = [PS5_weighted_polarity_data, Series_X_weighted_polarity_data]
plt.boxplot(console_weighted_polarity_array, 
            showmeans = True, 
            meanprops={"marker": "o", 
                       "markerfacecolor": "black", 
                       "markeredgecolor": "black"})
plt.title("Box-and-Whisker Plot: Next-Gen Weighted Polarity Values")
plt.xticks([1,2], ["PS5", "Series X"])
plt.xlabel("Next-Gen Console")
plt.ylabel("weighted polarity")
plt.show()

# Isolate subjectivity data for both the PS5 and the Series X
PS5_subjectivity_data = twitter_data_PS5.subjectivity
Series_X_subjectivity_data = twitter_data_Series_X.subjectivity

# Acquire weighted 5-number summary and mean for subjectivity scores for the PS5
PS5_retweet_count_data = twitter_data_PS5.retwc

array_for_weighted_stats_PS5_subjectivity = np.repeat(PS5_subjectivity_data, 
                                                  PS5_retweet_count_data)
# print(array_for_weighted_stats_PS5_subjectivity)

# Acquire weighted 5-number summary and mean for subjectivity scores for the PS5

PS5_subjectivity_weighted_Min = array_for_weighted_stats_PS5_subjectivity.min()
PS5_subjectivity_weighted_LQ = np.percentile(array_for_weighted_stats_PS5_subjectivity, 25)
PS5_subjectivity_weighted_Median = np.percentile(array_for_weighted_stats_PS5_subjectivity, 50)
PS5_subjectivity_weighted_UQ = np.percentile(array_for_weighted_stats_PS5_subjectivity, 75)
PS5_subjectivity_weighted_Max = array_for_weighted_stats_PS5_subjectivity.max()

print("\n")

print("PS5 Subjectivity Weighted Min = " + str(PS5_subjectivity_weighted_Min))
print("PS5 Subjectivity Weighted Lower Quartile = " + str(PS5_subjectivity_weighted_LQ))
print("PS5 Subjectivity Weighted Median = " + str(PS5_subjectivity_weighted_Median))
print("PS5 Subjectivity Weighted Upper Quartile = " + str(PS5_subjectivity_weighted_UQ))
print("PS5 Subjectivity Weighted Max = " + str(PS5_subjectivity_weighted_Max))

# print("\n")

weighted_mean_PS5_subjectivity = array_for_weighted_stats_PS5_subjectivity.mean()
print("Weighted mean for PS5 subjectivity scores: " + 
      str(round(weighted_mean_PS5_subjectivity, 2)))

# reference_weighted_mean_PS5_subjectivity = round(np.average(PS5_subjectivity_data, 
#                                               weights = PS5_retweet_count_data), 2)
# print("Reference Calculation of Weighted mean for PS5 polarity scores: " + 
#       str(round(reference_weighted_mean_PS5_subjectivity, 2)))

# Acquire weighted 5-number summary and mean for polarity scores for the Series X
Series_X_retweet_count_data = twitter_data_Series_X.retwc

array_for_weighted_stats_Series_X_subjectivity = np.repeat(Series_X_subjectivity_data, 
                                                  Series_X_retweet_count_data)

# print(array_for_weighted_stats_Series_X_polarity)

# Acquire weighted 5-number summary and mean for subjectivity scores for the Series X

Series_X_subjectivity_weighted_Min = array_for_weighted_stats_Series_X_subjectivity.min()
Series_X_subjectivity_weighted_LQ = np.percentile(array_for_weighted_stats_Series_X_subjectivity, 25)
Series_X_subjectivity_weighted_Median = np.percentile(array_for_weighted_stats_Series_X_subjectivity, 50)
Series_X_subjectivity_weighted_UQ = np.percentile(array_for_weighted_stats_Series_X_subjectivity, 75)
Series_X_subjectivity_weighted_Max = array_for_weighted_stats_Series_X_subjectivity.max()

print("\n")

print("Series X Subjectivity Weighted Min = " + str(Series_X_subjectivity_weighted_Min))
print("Series X Subjectivity Weighted Lower Quartile = " + str(Series_X_subjectivity_weighted_LQ))
print("Series X Subjectivity Weighted Median = " + str(Series_X_subjectivity_weighted_Median))
print("Series X Subjectivity Weighted Upper Quartile = " + str(Series_X_subjectivity_weighted_UQ))
print("Series X Subjectivity Weighted Max = " + str(Series_X_subjectivity_weighted_Max))

# print("\n")

weighted_mean_Series_X_subjectivity = array_for_weighted_stats_Series_X_subjectivity.mean()
print("Weighted mean for Series X subjectivity scores: " + 
      str(round(weighted_mean_Series_X_subjectivity, 2)))

# reference_weighted_mean_Series_X_subjectivity = round(np.average(Series_X_subjectivity_data, 
#                                               weights = Series_X_retweet_count_data), 2)
# print("Reference Calculation of Weighted mean for PS5 polarity scores: " + 
#       str(round(reference_weighted_mean_Series_X_subjectivity, 2)))

print("\n")

# Showcase box-and-whisker plot for weighted subjectivity values of each console
PS5_weighted_subjectivity_data = array_for_weighted_stats_PS5_subjectivity
Series_X_weighted_subjectivity_data = array_for_weighted_stats_Series_X_subjectivity

plt.figure()
console_weighted_subjectivity_array = [PS5_weighted_subjectivity_data, Series_X_weighted_subjectivity_data]
plt.boxplot(console_weighted_subjectivity_array, 
            showmeans = True, 
            meanprops={"marker": "o", 
                       "markerfacecolor": "black", 
                       "markeredgecolor": "black"})
plt.title("Box-and-Whisker Plot: Next-Gen Weighted Subjectivity Values")
plt.xticks([1,2], ["PS5", "Series X"])
plt.xlabel("Next-Gen Console")
plt.ylabel("weighted polarity")
plt.show()

# ----

# Look at a correlation table for all of the data collected for each of the 
# gaming consoles

# correlation for the first Twitter search - PlayStation 5
twitter_data_PS5 = pd.read_csv(firstTwitterSearchResult)
print("\n")
print("Correlation matrix for variables associated with Tweets relating to the PlayStation 5")
# print("\n")
print(twitter_data_PS5.corr())

# correlation for the first Twitter search - Xbox Series X
twitter_data_Series_X = pd.read_csv(secondTwitterSearchResult)
print("\n")
print("Correlation matrix for variables associated with Tweets relating to the Xbox Series X")
# print("\n")
print(twitter_data_Series_X.corr())

# Next, attempt to plot a scatterplot for each of the gaming consoles...

# scatterplot of 'subjectivity' vs. 'polarity' for the PS5
plt.figure()
plt.scatter(twitter_data_PS5.polarity, 
            twitter_data_PS5.subjectivity, alpha = 0.25)
plt.title("Scatterplot 1a: 'subjectivity' vs. 'polarity' for the PS5")
plt.xlabel("polarity")
plt.ylabel("subjectivity")

# scatterplot of 'subjectivity' vs. 'polarity' for the Series X
plt.figure()
plt.scatter(twitter_data_Series_X.polarity, 
            twitter_data_Series_X.subjectivity, alpha = 0.25)
plt.title("Scatterplot 1b: 'subjectivity' vs. 'polarity' for the Series X")
plt.xlabel("polarity")
plt.ylabel("subjectivity")