from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Book dataset from the original Python project
data = {
    "Book": [
        "Harry Potter",
        "The Hobbit",
        "The Lord of the Rings",
        "Atomic Habits",
        "The Power of Habit",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Think and Grow Rich"
    ],
    "Fantasy": [10, 9, 10, 0, 0, 0, 2, 0],
    "Adventure": [9, 10, 9, 0, 0, 0, 8, 0],
    "Self_Help": [0, 0, 0, 10, 9, 5, 5, 8],
    "Business": [0, 0, 0, 2, 3, 10, 2, 9],
    "Personal_Development": [1, 1, 1, 10, 9, 8, 8, 10]
}

df = pd.DataFrame(data)
FEATURES = [
    "Fantasy",
    "Adventure",
    "Self_Help",
    "Business",
    "Personal_Development"
]

# Original, local illustrations keep book artwork available offline.
BOOK_INFO = {
    "Harry Potter": {"genre": "Fantasy • Magic • Adventure", "emoji": "⚡", "cover": "purple", "image": "harry-potter.svg"},
    "The Hobbit": {"genre": "Fantasy • Adventure", "emoji": "🐉", "cover": "green", "image": "the-hobbit.svg"},
    "The Lord of the Rings": {"genre": "Fantasy • Epic Adventure", "emoji": "💍", "cover": "gold", "image": "lord-of-the-rings.svg"},
    "Atomic Habits": {"genre": "Self-help • Habits", "emoji": "🌱", "cover": "mint", "image": "atomic-habits.svg"},
    "The Power of Habit": {"genre": "Psychology • Self-help", "emoji": "🧠", "cover": "blue", "image": "power-of-habit.svg"},
    "Rich Dad Poor Dad": {"genre": "Business • Finance", "emoji": "💰", "cover": "orange", "image": "rich-dad-poor-dad.svg"},
    "The Alchemist": {"genre": "Fiction • Adventure", "emoji": "✨", "cover": "pink", "image": "the-alchemist.svg"},
    "Think and Grow Rich": {"genre": "Personal development • Business", "emoji": "🚀", "cover": "navy", "image": "think-and-grow-rich.svg"}
}

def recommend_books(book_name):
    """Return the top 3 books most similar to the selected book."""
    selected = df[df["Book"].str.lower() == book_name.strip().lower()]
    if selected.empty:
        return None

    selected_title = selected.iloc[0]["Book"]
    similarity = cosine_similarity(selected[FEATURES], df[FEATURES])[0]

    results = []
    for idx, score in enumerate(similarity):
        title = df.iloc[idx]["Book"]
        if title.lower() == selected_title.lower():
            continue
        info = BOOK_INFO.get(title, {})
        results.append({
            "title": title,
            "score": round(float(score) * 100, 2),
            "genre": info.get("genre", "Book"),
            "emoji": info.get("emoji", "📘"),
            "cover": info.get("cover", "navy"),
            "image": info["image"]
        })

    results.sort(key=lambda item: item["score"], reverse=True)
    return {
        "selected": {
            "title": selected_title,
            **BOOK_INFO.get(selected_title, {})
        },
        "recommendations": results[:3]
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    query = ""

    if request.method == "POST":
        query = request.form.get("book_name", "").strip()
        if not query:
            error = "Please enter or select a book name."
        else:
            result = recommend_books(query)
            if result is None:
                error = "We couldn't find that book. Please choose a title from the available list."

    books = [
        {
            "title": row["Book"],
            **BOOK_INFO.get(row["Book"], {})
        }
        for _, row in df.iterrows()
    ]
    return render_template(
        "index.html",
        books=books,
        result=result,
        error=error,
        query=query
    )

if __name__ == "__main__":
    app.run(debug=True)
