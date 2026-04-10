import joblib
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/triage.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fallback_logic(text, confidence):
    # Too short to classify reliably
    if len(text.split()) < 3:
        return "Too vague – please provide more detail."

    # Model is not confident enough
    if confidence < 0.25:
        return "Needs human review."

    return None


def assign_priority(text, category, confidence):
    text_lower = text.lower()
    score = 0

    # Impact keywords (+3)
    if any(word in text_lower for word in ["down", "not working", "cannot display", "no display", "outage", "offline"]):
        score += 3

    # High severity keywords (+2)
    if any(word in text_lower for word in ["critical", "urgent", "immediately", "emergency"]):
        score += 2

    # Medium severity keywords (+1)
    if any(word in text_lower for word in ["slow", "intermittent", "unstable", "lagging"]):
        score += 1

    # Low severity keywords (-1)
    if any(word in text_lower for word in ["request", "setup", "install", "new account", "access needed"]):
        score -= 1

    # Category weighting
    if category == "Network":
        score += 2
    elif category == "Access":
        score += 1
    elif category == "Hardware":
        score += 1
    elif category == "Software":
        score += 0

    # Confidence modifier (small influence, not override)
    if confidence > 0.80:
        score += 1
    elif confidence < 0.40:
        score -= 1

    # Final score → priority
    if score >= 6:
        return "High"
    elif score >= 3:
        return "Medium"
    else:
        return "Low"



def classify_incident(text):
    # Load model + vectorizer
    model = joblib.load("models/model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")

    # Vectorize input
    vectorized = vectorizer.transform([text])

    # Predict probabilities
    probs = model.predict_proba(vectorized)[0]
    confidence = max(probs)
    category = model.classes_[probs.argmax()]

    # Apply fallback logic
    fallback = fallback_logic(text, confidence)
    if fallback:
        logging.info(
            f"Input='{text}' | Category=None | Confidence={confidence:.3f} | "
            f"Priority=None | Fallback='{fallback}'"
        )
        return {
            "category": None,
            "confidence": round(confidence, 3),
            "priority": None,
            "fallback": fallback
        }

    # Apply priority logic
    priority = assign_priority(text, category, confidence)

    # Log successful classification
    logging.info(
        f"Input='{text}' | Category='{category}' | Confidence={confidence:.3f} | "
        f"Priority='{priority}' | Fallback=None"
    )

    # Final structured output
    return {
        "category": category,
        "confidence": round(confidence, 3),
        "priority": priority,
        "fallback": None
    }



if __name__ == "__main__":
    user_input = input("Describe the incident: ")
    result = classify_incident(user_input)
    print(result)
