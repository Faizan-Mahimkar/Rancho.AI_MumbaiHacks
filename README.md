## Features

- *Budget Tracking*: Users can input their income and expenses to receive budgeting suggestions.
- *Investment Advice*: Provides personalized investment recommendations based on user goals and risk tolerance.
- *Saving Tips*: Offers strategies for saving money, including setting saving goals and tracking progress.
- *Financial Education*: Answers common financial questions and provides educational resources.

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js
- npm (Node Package Manager)
- SQLite

### Backend Setup

1. *Create and activate a virtual environment:*

    bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

2. *Install the required packages:*

    bash
    pip install -r backend/requirements.txt
    

3. *Initialize the database:*

    bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    

4. *Run the Flask app:*

    bash
    python backend/run.py
    

### Frontend Setup

1. **Navigate to the frontend directory:**

    bash
    cd frontend
    

2. *Install the dependencies:*

    bash
    npm install
    

3. *Start the frontend:*

    bash
    npm start
    

4. **Open public/index.html in your web browser:**

    You can now interact with the chatbot interface.

### Database

1. *Set up the database schema:*

    The database schema is defined in database/schema.sql.

    bash
    sqlite3 app.db < database/schema.sql
    

2. *Seed the database with initial data:*

    bash
    python database/seed.py
    

## Usage

- Open the frontend in your web browser.
- Enter your username and type a message to interact with the chatbot.
- The chatbot will respond with personalized financial advice based on your input.

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Hugging Face](https://huggingface.co/)
- [GPT-2 Model](https://huggingface.co/gpt2)
- [SQLite](https://www.sqlite.org/index.html)
- [Node.js](https://nodejs.org/)
- [Bootstrap](https://getbootstrap.com/)
