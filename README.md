# Milestone.Ai

This project is a comprehensive software solution for managing an educational environment, enabling instructors to track students' progress through various APIs, data handling, and frontend interfaces. It includes backend services for handling AI-powered analysis, milestones, and secure data operations, along with a user-friendly frontend for instructors and students.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Documentation](#documentation)
- [Assets](#assets)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure

```
.
├── assets/               # Contains image assets used in the project (login screens, etc.)
├── backend/              # Backend service for API handling and data management
│   ├── app/              # Main application code
│   │   ├── AI_service/   # Services related to AI and LLM (Large Language Model) operations
│   │   │   ├── api/      # APIs for code analysis, PDF analysis, best practices, etc.
│   │   │   ├── controllers/  # Controllers for milestone generation, PDF and GitHub analysis
│   │   │   ├── guard/    # Security configurations
│   │   │   ├── llm_ops/  # Operations related to language models
│   │   │   └── schema/   # Schema definitions for milestone and coding guidelines
│   │   ├── config/       # Configurations, including logging
│   │   ├── database/     # Database-related files
│   │   ├── dump/         # Temporary data dumps in Markdown and PDF formats
│   │   ├── log/          # Logging information
│   │   └── main.py       # Main file to run the backend server
│   ├── README.md         # Backend-specific README
│   └── requirements.txt  # Backend dependencies
├── docs/                 # Documentation for the project
├── frontend/             # Frontend service for user interface
└── UI/                   # Additional user interface components
```

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.9+
- Node.js (for frontend)
- pip (Python package manager)

### Setup

1. **Clone the repository:**

   ```bash
   git clone <repo_url>
   cd <repo_folder>
   ```

2. **Backend Installation:**

   Navigate to the backend directory and install the dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Frontend Installation:**

   Navigate to the frontend directory and install the dependencies:

   ```bash
   cd frontend
   npm install
   ```

## Usage

### Running the Backend Server

From the `backend` folder, run:

```bash
uvicorn app.main:app --reload
```

This will start the backend server locally on `http://localhost:8000`.

### Running the Frontend Server

From the `frontend` folder, run:

```bash
npm start
```

This will start the frontend server on `http://localhost:3000`.

## API Endpoints

The backend APIs are organized to support various functionalities in this educational platform. Key endpoints include:

- **/analyze_code**: Analyzes provided code and returns insights.
- **/analyze_pdf**: Analyzes a PDF document and extracts relevant information.
- **/generate_milestones**: Creates milestones based on project details.
- **/best_practices**: Suggests coding best practices.

For a full list of API endpoints and their details, refer to `backend/app/AI_service/api/`.

## Documentation

Documentation for the project is located in the `docs/` folder, including API specifications, architecture, and guides for usage.

## Assets

The `assets/` folder contains visual resources, including:

- Login page for instructors and students
- Registration screenshots

These assets are primarily used in the frontend for user interface designs.

## Contributing

To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to the branch.
4. Open a pull request and describe your changes.

Please make sure to follow the [contributing guidelines](docs/CONTRIBUTING.md) (if available).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
