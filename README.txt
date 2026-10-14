PAGETURNER - BOOK RECOMMENDATION WEBSITE

WHAT THIS PROJECT DOES
- Uses your sample book dataset.
- Uses cosine similarity from scikit-learn.
- Lets users search for a book or click a book from the collection.
- Displays the top 3 similar books and a similarity percentage.
- Runs as a local Flask website.

REQUIREMENTS
- Python 3.10 or newer recommended
- Internet is only needed to install packages and load optional Google Fonts.
  Original SVG book illustrations are stored locally and work offline.

HOW TO RUN ON WINDOWS
1. Extract this ZIP file.
2. Open the extracted folder in VS Code, or open Command Prompt in this folder.
3. Create a virtual environment (recommended):
      py -m venv .venv
4. Activate it:
      .venv\\Scripts\\activate
5. Install dependencies:
      python -m pip install -r requirements.txt
6. Start the website:
      python app.py
7. Open this address in your browser:
      http://127.0.0.1:5000

HOW TO RUN ON UBUNTU / LINUX
1. Open Terminal in the extracted project folder.
2. Create and activate a virtual environment:
      python3 -m venv .venv
      source .venv/bin/activate
3. Install dependencies:
      python -m pip install -r requirements.txt
4. Start the website:
      python app.py
5. Open this address in your browser:
      http://127.0.0.1:5000

TEST IT
Try "Harry Potter", "The Hobbit", "Atomic Habits", or any book shown on the homepage.
Book titles are matched without case sensitivity, so "harry potter" also works.

NOTE
This project intentionally keeps the original 8-book sample dataset and feature-based
cosine similarity algorithm. Its original SVG illustrations are stored in static/images;
they are not official book cover images. For production use, turn off Flask debug mode
and use a larger, properly sourced dataset.
