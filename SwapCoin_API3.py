

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Simulated database of API keys and secrets for authentication
api_credentials = {
    "YOUR_API_KEY": "YOUR_API_SECRET"
}

api_endpoint = "https://api.raydium.io/swap/v3"

@app.route('/BuySwapGoodCoin', methods=['GET'])
def transaction_summary():
    
    # collect all values
    api_key = request.args.get('api_key', default=None, type=str)
    api_secret = request.args.get('api_secret', default=None, type=str)
    input_token = request.args.get('input_token', default=None, type=str)
    input_amount = request.args.get('input_amount', default=None, type=str)
    out_token = request.args.get('out_token', default=None, type=str)
    out_amount = request.args.get('out_amount', default=None, type=str)

    print (f'Api Key : {api_key}')
    print (f'Secret Key : {api_secret}')
    print (f'Input Token : {input_token}')
    print (f'Input Amount : {input_amount}')
    print (f'Out Token : {out_token}')
    print (f'Out Amount : {out_amount}')



    if api_key is None or api_secret is None or input_token is None or input_amount is None or out_token is None or out_amount is None:
        return jsonify({'error': 'All Values are required'}), 400
    # Authenticate the API key and secret
    # if not authenticate_api_key(api_key, api_secret):
    #     return jsonify({"error": "Authentication failed"}), 403

    # # Process the token swap
    transaction_success = process_swap(input_token, input_amount, out_token, out_amount, api_key, api_secret)

    # Prepare the response based on the transaction result
    result = "Success" if transaction_success else "Fail"
    response = {
        "InputToken": input_token,
        "Output": [
            {
                "Result": result
            }
        ]
    }
    
    return jsonify(response)

# def authenticate_api_key(api_key, api_secret):
#     """ Validate the API key and secret. """
#     return api_credentials.get(api_key) == api_secret

def process_swap(input_token, input_amount, output_token, min_output_amount, api_key, api_secret):
    """ Simulate a token swap transaction. This is just a placeholder for your business logic. """
    # Example business logic: check if input_amount meets some criteria
    
    payload = {
    "inputToken": input_token,
    "inputAmount": input_amount,
    "outputToken": output_token,
    "minOutputAmount": min_output_amount
    }

    # Set API request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "X-Raydium-API-Key": api_key,
        "X-Raydium-API-Secret": api_secret
    }

    # Send API request
    response = requests.post(api_endpoint, json=payload, headers=headers)

    # Check API response status code
    if response.status_code == 200:
        #print("Swap successful!")
        return True
    else:
        #print("Swap failed!")
        return False

    
    #     if float(input_amount) >= 100:  # Assume 100 is the minimum amount needed for the swap
    #         return True  # Transaction successful
    # return False  # Transaction failed



if __name__ == '__main__':
    app.run(debug=False)


 # app.run(debug=False, host='0.0.0.0', port=5000)




####http://127.0.0.1:5000/BuySwapGoodCoin?api_key={api_key}&api_secret={api_secret}&input_token={input_token}&input_amount={input_amount}&out_token={out_token}&out_amount={out_amount}

# Replace https://127.0.0.1:5000 with your actual app's URL.









