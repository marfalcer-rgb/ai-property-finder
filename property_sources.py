PROPERTY_SOURCES = {
    "USA Government Real Estate": "https://www.usa.gov/real-estate-sales",
    "HUD": "https://www.hud.gov/homes",
    "Treasury": "https://www.treasury.gov/auctions/treasury/rp/",
}

print("Property sources loaded:")
for name, url in PROPERTY_SOURCES.items():
    print(name, "->", url)