from gpt4all import GPT4All

model_path = "C:/Users/mraja/OneDrive/Desktop/.gpt4all/models"
model_name = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

model = GPT4All(
    model_name=model_name,
    model_path=model_path,
    allow_download=False
)

def get_medicine_explanation(medicine_name):
    prompt = (
        f"You are a helpful AI assistant. Please explain the medicine '{medicine_name}' in simple terms, "
        f"including what it is for, how to take it, and any side effects."
    )
    
    with model.chat_session() as session:
        response = session.generate(prompt, max_tokens=300)
    
    return response
