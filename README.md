# MathSpace
AI Mathematics Intelligence Platform.

## Stack
- Frontend: TypeScript + React + Next.js + Tailwind CSS
- Backend: Python + FastAPI
- AI/ML: Python + PyTorch-ready services
- LLM: Python AI provider abstraction
- Mathematics: NumPy + SymPy
- Database: PostgreSQL + SQLAlchemy
- Authentication: JWT-ready Python backend
- Mobile: Flutter/Dart starter
- Real-time: WebSocket
- Deployment: Docker
- Testing: Pytest + Vitest

## Start
### Backend
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000 and API docs at http://127.0.0.1:8000/docs.

### Docker
```bash
docker compose up --build
```
