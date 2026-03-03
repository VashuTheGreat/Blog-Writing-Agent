# ✍️ Bloggig - AI Blog Writing Agent

Bloggig is a sophisticated AI-powered agent designed to transform a single topic into a professional, research-backed blog post complete with AI-generated visuals. Built with **LangGraph** and **FastAPI**, it orchestrates a complex pipeline of research, planning, writing, and image generation to deliver high-quality content in real-time.

![Bloggig Preview](graph.png)

## 🚀 Key Features

- **🌐 Autonomous Research**: Integrates with Tavily AI to perform deep web searches and gather factual evidence.
- **📋 Intelligent Planning**: Generates structured blog plans tailored to specific audiences and tones.
- **✍️ Parallel Writing Pipeline**: Uses a worker-reducer architecture to generate multiple blog sections simultaneously for maximum efficiency.
- **🎨 AI-Generated Visuals**: Automatically plans and generates relevant images using **Stable Diffusion XL** (via Hugging Face Inference).
- **💻 Modern ChatGPT-like UI**: A sleek, dark-themed dashboard featuring:
  - **Real-time Streaming**: Watch the AI's "thought process" and pipeline progression via WebSockets.
  - **Markdown Rendering**: Beautifully formatted blog previews with syntax highlighting.
  - **History Management**: Browse, view, and manage previously generated blogs.
- **📦 Export & Management**:
  - **Download as ZIP**: Get the full markdown file along with all generated image assets.
  - **Clean Deletion**: Permanent removal of blogs and their associated images with a single click.

## 🛠️ Tech Stack

- **Backend**: FastAPI, LangGraph, Pydantic, Uvicorn.
- **AI Models**: Bedrock Converse API (LLM), Stable Diffusion XL (Images).
- **Search Engine**: Tavily AI.
- **Frontend**: Semantic HTML5, Vanilla CSS (Glassmorphism), Marked.js, Highlight.js.
- **Tools**: UV (Python package manager), Git.

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/VashuTheGreat/Blog-Writing-Agent.git
cd Blog-Writing-Agent
```

### 2. Install Dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the root directory and add your credentials:

```env
HF_TOKEN=your_huggingface_token
TAVILY_API_KEY=your_tavily_api_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=your_aws_region
```

## 🏃 Running the Application

Start the FastAPI server:

```bash
python Application/app.py
```

The application will be available at `http://localhost:8000`.

## 📂 Project Structure

- `Application/`: Contains the web server (`app.py`) and the frontend (`index.html`).
- `src/graph/`: Core LangGraph implementation (nodes, edges, and logic).
- `src/components/`: External integrations (Tavily search, Image generation).
- `src/models/`: Pydantic models for state management and structured output.
- `results/`: Directory where generated markdown blogs are saved.
- `images/`: Directory where generated images are stored.
- `src/utils/`: Utility functions (e.g., blog deletion logic).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
