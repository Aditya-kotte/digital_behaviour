import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("panda_behavior.csv")
df["Day_label"] = [f"D{i+1}" for i in range(len(df))]



# plt.bar(df["Date"],df["Total_Screen_Time"])
# # plt.xlabel("Date")
# # plt.ylabel("Total_screen_time")
# plt.title("My Screen Time by Day")
# plt.xlabel("Day")
# plt.ylabel("Minutes")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# plt.savefig("total_screen_time_chart.png")
# plt.close()

#chart2
# apps = ["Instagram", "YouTube", "WhatsApp", "LinkedIn"]
# totals = [df["Instagram_Minutes"].sum(),df["YouTube_Minutes"].sum(),df["WhatsApp_Minutes"].sum(), df["LinkedIn_Minutes"].sum()]
# plt.figure()
# plt.bar(apps,totals,color="black")
# plt.title("Total Time by App")
# plt.xlabel("App")
# plt.ylabel("Minutes")

# plt.show()
# plt.savefig("total_time_by_app.png")
# plt.close()


#chart3
# plt.figure(figsize=(12,5))
# plt.plot(df["Date"],df["Study_Minutes"],label = "Study Minutes")
# plt.plot(df["Date"],df["Total_Screen_Time"],label = "Total screen time")
# plt.xlabel("Day")
# plt.ylabel("Minutes")
# plt.title("Study time vs Screen time")

# plt.legend()
# plt.show()

#chart4

apps = ["Instagram", "YouTube", "WhatsApp", "LinkedIn"]
totals = [df["Instagram_Minutes"].sum(),df["YouTube_Minutes"].sum(),df["WhatsApp_Minutes"].sum(), df["LinkedIn_Minutes"].sum()]
plt.pie(totals,label = apps,autopct = "%1.1f%%")
plt.title("Share of Total app Time")
plt.show()

