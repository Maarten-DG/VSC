def create_supplier(delay_factor, price_factor):
    # We definiëren een nieuwe functie binnenin
    def calculate_offer(expected_delivery_time, price_estimate):
        # Deze functie gebruikt de factoren van de 'moederfunctie'
        final_delivery = expected_delivery_time * delay_factor
        final_price = price_estimate * price_factor
        
        print(f"geschatte levertijd: {int(final_delivery)} dagen")
        print(f"geschatte kostprijs: {int(final_price)} euro")
    
    # We geven de functie zelf terug, niet het resultaat van de functie!
    return calculate_offer

# --- Test code ---
get_offer_from_bol = create_supplier(0.8, 1.1)
get_offer_from_amazon = create_supplier(1.2, 0.9)
get_offer_from_aliexpress = create_supplier(1.5, 0.75)

print("Bol.com offerte:")
get_offer_from_bol(100, 100)

print("\nAmazon offerte:")
get_offer_from_amazon(100, 100)

print("\nAliExpress offerte:")
get_offer_from_aliexpress(100, 100)