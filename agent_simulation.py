import pandas as pd
import os

from generate_garbage import generate_garbage_data

def simulate_agent_response(query, data_path):
    """
    A simple "RAG-like" simulation. 
    It looks for the best match in the data and returns a response.
    """
    try:
        df = pd.read_csv(data_path)
        
        # Simple Logic: Look for the product with highest price or matching category
        if "electronic" in query.lower():
            subset = df[df['category'].str.lower() == 'electronics']
            if not subset.empty:
                best_deal = subset.loc[subset['price'].idxmax()]
                return f"Agent: Based on my data, the best choice is {best_deal['product']} at ${best_deal['price']}."
            else:
                return "Agent: Sorry, I don't see any electronics in my current knowledge base."
        
        return "Agent: I'm not sure how to answer that with the current data."
        
    except Exception as e:
        return f"Agent Error: I'm choking on the data! ({str(e)})"

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    clean_data_path = os.path.join(base_dir, "processed_data.csv")
    garbage_data_path = os.path.join(base_dir, "garbage_data.csv")

    if not os.path.exists(garbage_data_path):
        generate_garbage_data()

    # Test with Clean Data
    print("Testing with CLEAN data:")
    print(
        simulate_agent_response(
            "What is the best electronic product?",
            clean_data_path,
        )
    )
    
    # Test with Garbage Data (to be created by students)
    print("\nTesting with GARBAGE data:")
    print(
        simulate_agent_response(
            "What is the best electronic product?",
            garbage_data_path,
        )
    )
