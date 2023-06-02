import ssl
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Function to generate AI response


def generate_response(question):
    response = openai.Completion.create(
        engine='davinci',  # Choose the appropriate engine
        prompt=question,
        max_tokens=100,  # Adjust as needed
        n=1,  # Number of responses to generate
        stop=None,  # Stop generation at a specific token (optional)
        temperature=0.7  # Controls the randomness of the response
    )
    return response.choices[0].text.strip()


# Example usage
user_question = input("Ask a question: ")
ai_response = generate_response(user_question)
print(ai_response)
