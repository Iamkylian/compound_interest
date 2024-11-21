import pandas as pd

# Flatten results into a list of dictionaries for DataFrame construction
data = []
for rate, rate_results in results.items():
    for period, period_results in rate_results.items():
        for duration, amount in period_results.items():
            data.append({
                "Taux (%)": rate,
                "Fréquence": period,
                "Durée (ans)": duration,
                "Montant final (€)": amount
            })

# Create a DataFrame
df = pd.DataFrame(data)

# Generate the table in landscape format
df_landscape = df.pivot_table(
    index=["Taux (%)", "Durée (ans)"], 
    columns="Fréquence", 
    values="Montant final (€)", 
    aggfunc="first"
).reset_index()

# Return the table for the screenshot
df_landscape
