from src.model import train_model
from src.preprocess import clean_text
from src.priority import assign_priority


model, vectorizer = train_model()

print("=== Support Ticket Classification System ===")

while True:
    user_input = input("\nEnter support ticket (or type 'exit'): ")

    if user_input.lower() == 'exit':
        print("Exiting system...")
        break

    cleaned = clean_text(user_input)
    vector = vectorizer.transform([cleaned])

    category = model.predict(vector)[0]
    priority = assign_priority(user_input)

    print("\n--- Result ---")
    print("Category:", category)
    print("Priority:", priority)