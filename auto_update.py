import os
from datetime import datetime

# List of all pairs to update
pairs = ['USDINR', 'USDBRL', 'NZDCAD', 'USDTRY', 'USDMXN']
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append update line to each JSON
for pair in pairs:
    try:
        with open(f"{pair}.json", "a") as f:
            f.write(f'\nUpdated on {now}')
    except Exception as e:
        print(f"Error updating {pair}.json: {e}")

# Git push commands
os.system("git add .")
os.system(f'git commit -m "Auto update at {now}"')
os.system("git push")
