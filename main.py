from carbot import CarInsightsAI
def main():
    """Example usage of the Car Insights AI"""

    # Initialize the AI with your dataset
    car_ai = CarInsightsAI()
    
    # Load your specific dataset
    car_ai.load_dataset('Car details v3.csv')
    
    print("Car Insights AI Chatbot")
    print("=" * 50)
    print("Dataset: Car details v3")
    print("Example interactions:")
    print("- 'Hello'")
    print("- 'Cars under 50000'")
    print("- 'Show me the cheapest car'")
    print("- 'Diesel cars under 100000'")
    print("- 'Automatic 5 seater cars'")
    print("- 'Compare Swift vs Baleno'")
    print("- 'more cars' (after any search)")
    print("=" * 50)
    print("- 'Cars under 30000' or 'Cars between 50000 and 100000'")
    print("- Fuel type search: 'petrol cars' or 'diesel cars'")
    print("- Transmission search: 'automatic cars' or 'manual cars'")
    print("- '5 seater cars' or '7 seat cars'")
    print("- Find cheapest/most expensive cars")
    print("- Brand counting")
    print("- Car comparisons and recommendations")
    print("=" * 50)
    
    # Interactive loop
    last_query = None
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            break
        
        # Store last query for "more cars" functionality
        if not any(phrase in user_input.lower() for phrase in ['more cars', 'hello', 'hi', 'bye', 'goodbye']):
            if not user_input.strip().isdigit():  # Don't store number selections as queries
                last_query = user_input
        
        response = car_ai.respond(user_input, last_query)
        print(f"\nCarBot: {response}")

if __name__ == "__main__":
    main()
