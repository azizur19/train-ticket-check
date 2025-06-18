import pandas as pd

# Data organized by category
data = [
    # Police
    {"Category": "Police", "Rank": 1, "Title": "Inspector General of Police (IGP)"},
    {"Category": "Police", "Rank": 2, "Title": "Additional Inspector General of Police"},
    {"Category": "Police", "Rank": 3, "Title": "Deputy Inspector General (DIG)"},
    {"Category": "Police", "Rank": 4, "Title": "Additional DIG"},
    {"Category": "Police", "Rank": 5, "Title": "Superintendent of Police (SP)"},
    {"Category": "Police", "Rank": 6, "Title": "Additional SP"},
    {"Category": "Police", "Rank": 7, "Title": "Assistant Superintendent of Police (ASP)"},

    # Judges
    {"Category": "Judiciary", "Rank": 1, "Title": "Chief Justice of Bangladesh"},
    {"Category": "Judiciary", "Rank": 2, "Title": "Appellate Division Judge"},
    {"Category": "Judiciary", "Rank": 3, "Title": "High Court Division Judge"},
    {"Category": "Judiciary", "Rank": 4, "Title": "District and Sessions Judge"},
    {"Category": "Judiciary", "Rank": 5, "Title": "Additional District Judge"},
    {"Category": "Judiciary", "Rank": 6, "Title": "Joint District Judge"},
    {"Category": "Judiciary", "Rank": 7, "Title": "Senior Assistant Judge"},

    # Civil Administration
    {"Category": "Civil Administration", "Rank": 1, "Title": "Cabinet Secretary"},
    {"Category": "Civil Administration", "Rank": 2, "Title": "Principal Secretary to the Prime Minister"},
    {"Category": "Civil Administration", "Rank": 3, "Title": "Senior Secretary / Secretary"},
    {"Category": "Civil Administration", "Rank": 4, "Title": "Additional Secretary"},
    {"Category": "Civil Administration", "Rank": 5, "Title": "Joint Secretary"},
    {"Category": "Civil Administration", "Rank": 6, "Title": "Deputy Secretary"},
    {"Category": "Civil Administration", "Rank": 7, "Title": "Senior Assistant Secretary"},
    {"Category": "Civil Administration", "Rank": 8, "Title": "Assistant Secretary"},

    # Military
    {"Category": "Military", "Rank": 1, "Title": "Chief of Army Staff (General)"},
    {"Category": "Military", "Rank": 2, "Title": "Chief of Naval Staff (Admiral)"},
    {"Category": "Military", "Rank": 3, "Title": "Chief of Air Staff (Air Chief Marshal)"},
    {"Category": "Military", "Rank": 4, "Title": "Lieutenant General"},
    {"Category": "Military", "Rank": 5, "Title": "Major General"},
    {"Category": "Military", "Rank": 6, "Title": "Brigadier General"},

    # National Positions
    {"Category": "National", "Rank": 1, "Title": "President of Bangladesh"},
    {"Category": "National", "Rank": 2, "Title": "Prime Minister of Bangladesh"},
    {"Category": "National", "Rank": 3, "Title": "Speaker of the Parliament"},
    {"Category": "National", "Rank": 4, "Title": "Chief Election Commissioner"},
    {"Category": "National", "Rank": 5, "Title": "Attorney General"},
    {"Category": "National", "Rank": 6, "Title": "Comptroller and Auditor General (CAG)"},
    {"Category": "National", "Rank": 7, "Title": "Chairman, Anti-Corruption Commission (ACC)"},
    {"Category": "National", "Rank": 8, "Title": "Governor, Bangladesh Bank"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Add relevant websites to each row where applicable
websites = {
    "Police": "https://police.gov.bd",
    "Judiciary": "https://supremecourt.gov.bd",
    "Civil Administration": "https://cabinet.gov.bd",
    "Military": "https://mod.gov.bd",  # Ministry of Defence
    "National": "https://bangladesh.gov.bd",  # National portal
}

# Add a Website column by mapping from Category
df["Website"] = df["Category"].map(websites)

# Save updated CSV
csv_with_websites_path = "E:/__init__()/Code/Python/train_ticket/bd_high_rank_officials_with_websites.csv"
df.to_csv(csv_with_websites_path, index=False)
