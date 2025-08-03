# AI-Powered Career Guidance System

This project is an AI-powered career guidance system that helps users identify suitable tech roles based on their personality traits and skills. The system uses a machine learning model to predict career paths and provides a user-friendly web interface for interaction.

## Features

*   **Career Prediction:** Recommends tech roles based on user input of personality traits and skills.
*   **Interactive UI:** A modern, responsive web interface built with Next.js and shadcn/ui.
*   **Scalable Backend:** A Python-based backend to serve the machine learning model.
*   **Modular Structure:** The project is organized into frontend, backend, and model training components.

## Technologies Used

*   **Frontend:**
    *   [Next.js](https://nextjs.org/) - React framework for building user interfaces.
    *   [TypeScript](https://www.typescriptlang.org/) - Typed superset of JavaScript.
    *   [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework.
    *   [shadcn/ui](https://ui.shadcn.com/) - Re-usable components built using Radix UI and Tailwind CSS.
    *   [Axios](https://axios-http.com/) - Promise-based HTTP client for the browser and Node.js.

*   **Backend:**
    *   [Python](https://www.python.org/) - Programming language for the backend.
    *   [Flask](https://flask.palletsprojects.com/) / [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building APIs (based on `main.py`).
    *   [scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for Python.
    *   [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis library.

*   **Model Training:**
    *   [Jupyter Notebook](https://jupyter.org/) / Python Scripts - For model training and experimentation.
    *   [scikit-learn](https://scikit-learn.org/stable/) - For building and training the machine learning model.
    *   [Pandas](https://pandas.pydata.org/) - For data loading and preprocessing.

## Project Structure

```
AI-career-guidance-system/
├── backend/
│   ├── main.py
│   └── ...
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   └── ...
│   ├── components/
│   │   └── ...
│   ├── services/
│   │   └── api.ts
│   └── ...
├── model_training/
│   ├── data/
│   │   └── CareerMap- Mapping Tech Roles With Personality & Skills.csv
│   ├── scripts/
│   │   ├── train_model.py
│   │   └── predict.py
│   └── artifacts/
│       ├── model.pkl
│       └── label_encoder.pkl
└── README.md
```

## Getting Started

### Prerequisites

*   [Node.js](https://nodejs.org/en/) (v18 or later)
*   [pnpm](https://pnpm.io/installation)
*   [Python](https://www.python.org/downloads/) (v3.9 or later)
*   [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/AI-career-guidance-system.git
    cd AI-career-guidance-system
    ```

2.  **Install frontend dependencies:**

    ```bash
    cd frontend
    pnpm install
    ```

3.  **Install backend dependencies:**

    ```bash
    cd ../backend
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the backend server:**

    ```bash
    cd backend
    python main.py
    ```

    The backend server will start on `http://127.0.0.1:5000`.

2.  **Run the frontend development server:**

    ```bash
    cd frontend
    pnpm dev
    ```

    The frontend development server will start on `http://localhost:3000`.

3.  **Open your browser** and navigate to `http://localhost:3000` to use the application.

## Model Training

The machine learning model is trained to predict tech roles based on personality traits and skills. The training script and dataset are located in the `model_training` directory.

To retrain the model, run the following command:

```bash
cd model_training/scripts
python train_model.py
```

This will train a new model using the data in `model_training/data` and save the artifacts (`model.pkl` and `label_encoder.pkl`) in the `model_training/artifacts` directory.

## API Endpoints

The backend provides the following API endpoint:

*   **`POST /predict`**: Predicts a tech role based on user input.

    *   **Request Body:**
        ```json
        {
          "personality_traits": ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"],
          "skills": ["Python", "JavaScript", "Data Analysis"]
        }
        ```

    *   **Response:**
        ```json
        {
          "predicted_role": "Data Scientist"
        }
        ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
