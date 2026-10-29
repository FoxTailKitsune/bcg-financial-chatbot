from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# --- The Chatbot Logic ---
def simple_chatbot(user_query):
    # Convert query to lowercase to handle varying user inputs
    query = user_query.lower()
    
    # 1. Revenue Growth Query
    if "revenue growth" in query or "highest growth" in query:
        return ("Microsoft saw the highest revenue growth. Over the three-year period from 2023 to 2025, their revenue expanded at an average annual rate of 15.3%."
                " Apple had an average growth rate of 4.2%, while Tesla's revenue decreased at an average annual rate of 1.0%.")
    
    # 2. Total Revenue Query
    elif "total revenue" in query or "revenue for 2025" in query:
        return ("In 2025, Apple reported the highest total revenue at $416.2 billion, followed by Microsoft at $281.7 billion, and Tesla at $94.8 billion.")
    
    # 3. Net Income Change Query
    elif "net income changed" in query or "change in net income" in query:
        return ("From 2024 to 2025, Apple's net income grew by $18.3 billion and Microsoft's grew by $13.7 billion. In contrast, Tesla's net income declined by $3.3 billion.")
    
    # 4. Profit Margin Query
    elif "profit margin" in query or "profit margin" in query:
        return ("Microsoft has the highest net profit margin at 36.1% for 2025. This means for every dollar of revenue they generate, they keep about 36 cents in pure profit."
                " Apple has a net profit margin of 26.9%, and Tesla's net profit margin is 4.1%.")
    
    # 5. Solvency/Health Query
    elif "asset-to-liability" in query or "tesla's debt" in query:
        return ("Tesla's asset-to-liability ratio in 2025 is 2.51. This means they have about $2.51 in total assets for every $1 of liabilities, indicating a strong, safe, and well-capitalized balance sheet."
                " In comparison, Apple has a ratio of 1.26, and Microsoft has a ratio of 2.25.")
    
    # Fallback response
    else:
        return ("I can answer queries regarding total revenue, net income trends, profit margins, asset-to-liability ratios, and revenue growth for Apple, Microsoft, and Tesla.")
    
    
# --- Web Routes ---

# 1. Serve the homepage
@app.route("/")
def home():
    return render_template("index.html")

# 2. Handle the chat messages
@app.route("/chat", methods=["POST"])
def chat():
    # Receive the data from the frontend
    user_data = request.json
    user_message = user_data.get("message")
    
    # Process the message through our bot
    bot_reply = simple_chatbot(user_message)
    
    # Send the reply back to the frontend
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)