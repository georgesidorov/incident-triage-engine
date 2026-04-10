# Why These Methods?

The incident triage engine uses simple, reliable techniques because they work extremely well for short IT incident descriptions and do not require large datasets or heavy computing power. Each method was chosen to keep the system fast, understandable, and easy to maintain.

## How the text is turned into numbers (TF‑IDF)

Computers cannot understand words directly, so the system uses TF‑IDF to convert text into numbers. TF‑IDF looks at how often a word appears in a description and how rare or meaningful that word is across all incidents. Common words like “the” or “issue” get low importance, while more informative words like “outage”, “latency”, or “reset” get higher importance. This helps the model focus on the words that actually matter when deciding what type of incident it is.

## Why n‑grams improve understanding

Many IT issues are described using short phrases rather than single words. N‑grams capture these patterns by looking at pairs of words such as “server down”, “password reset”, or “email outage”. This gives the model a better sense of context and improves accuracy without adding complexity.

## Why Logistic Regression is used

Logistic Regression is a simple, fast machine‑learning model that works extremely well for text classification. It trains quickly, performs reliably on small datasets, and produces stable, interpretable results. For short IT incident descriptions, it performs just as well as more advanced models while being easier to maintain.

## Why the dataset is split into training and testing

Splitting the dataset ensures the model learns general patterns instead of memorising examples. The training set teaches the model, while the test set checks whether it can correctly classify new incidents it has never seen before.

## Why confidence scores matter

Each prediction includes a confidence score that shows how sure the model is. This helps the system decide whether to trust the prediction or rely more heavily on rule‑based logic. It prevents the model from making bold guesses when the input is unclear.

## Why rule‑based priority scoring is included

Machine‑learning models recognise patterns but do not understand urgency or business impact. Priority scoring fills this gap by using simple rules based on keywords and severity indicators. If a description contains words like “down”, “cannot access”, or “critical”, the system can raise the priority even if the model is unsure.

## Why fallback logic is essential

Some descriptions are too short, vague, or unusual for the model to classify confidently. Fallback logic ensures the system still returns a safe, sensible result rather than something random. This makes the tool more dependable in real‑world use.

## Why classical ML instead of deep learning

Deep learning models require large datasets, long training times, and more complex infrastructure. For short IT incident descriptions, classical machine‑learning provides almost the same accuracy with far less cost and complexity. It is easier to retrain, easier to debug, and easier to deploy, making it the right choice for a lightweight triage engine.
