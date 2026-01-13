import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Load dataset
# ==============================
df = pd.read_csv("weather_tokyo_data.csv")

# ==============================
# Auto-detect date column
# ==============================
date_col = None
for col in df.columns:
    if "date" in col.lower() or "time" in col.lower():
        date_col = col
        break

if date_col is None:
    raise ValueError("Nuk u gjet kolona e dates")

df[date_col] = pd.to_datetime(df[date_col])

# ==============================
# Auto-detect temperature column
# ==============================
temp_col = None
for col in df.columns:
    if "temp" in col.lower():
        temp_col = col
        break

if temp_col is None:
    raise ValueError("Nuk u gjet kolona e temperatures")

# ==============================
# 1. Temperature Overview
# ==============================
average_temperature = df[temp_col].mean()
print(f"Average Temperature (Overall): {average_temperature:.2f}")

# ==============================
# 2. Monthly Temperature
# ==============================
df['month'] = df[date_col].dt.month

monthly_avg_temperature = df.groupby('month')[temp_col].mean()
print("\nMonthly Average Temperature:")
print(monthly_avg_temperature)

# Monthly Average Bar Plot
plt.figure(figsize=(8,5))
plt.bar(monthly_avg_temperature.index, monthly_avg_temperature.values, color='skyblue')
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Monthly Average Temperature")
plt.tight_layout()
plt.show()

# ==============================
# 3. Highs and Lows
# ==============================
hottest_day = df.loc[df[temp_col].idxmax()]
coldest_day = df.loc[df[temp_col].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)

# ==============================
# 4. Temperature Trend Over Time
# ==============================
plt.figure(figsize=(10,5))
plt.plot(df[date_col], df[temp_col], color='orange')
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Trend Over Time")
plt.tight_layout()
plt.show()

# ==============================
# 5. Seasonal Average Temperature
# ==============================
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df['season'] = df['month'].apply(get_season)

seasonal_avg_temperature = df.groupby('season')[temp_col].mean()
print("\nSeasonal Average Temperature:")
print(seasonal_avg_temperature)

# Seasonal Average Bar Plot
plt.figure(figsize=(6,4))
plt.bar(seasonal_avg_temperature.index, seasonal_avg_temperature.values, color='green')
plt.xlabel("Season")
plt.ylabel("Average Temperature")
plt.title("Seasonal Average Temperature")
plt.tight_layout()
plt.show()

# ==============================
# 6. Daily Temperature Scatter Plot
# ==============================
plt.figure(figsize=(10,5))
plt.scatter(df[date_col], df[temp_col], s=10, alpha=0.5)
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Temperature Distribution")
plt.tight_layout()
plt.show()
