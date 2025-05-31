import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Fake road accident data
data = {
    'location': ['Highway 1', 'Highway 2', 'City Center', 'Highway 1', 'City Center'],
    'severity': ['High', 'Low', 'Medium', 'High', 'High'],
    'cause': ['Speeding', 'Rain', 'Signal Failure', 'Speeding', 'Drunk Driving']
}

df = pd.DataFrame(data)

# 🔍 Count accidents per location
location_counts = df['location'].value_counts()

# 🔍 Most common causes
cause_counts = df['cause'].value_counts()

# 📊 Plot location accidents
plt.figure(figsize=(8,4))
sns.barplot(x=location_counts.index, y=location_counts.values)
plt.title("Accidents by Location")
plt.xlabel("Location")
plt.ylabel("Number of Accidents")
plt.show()

print("Top accident causes:")
print(cause_counts)