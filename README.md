# YouTube GPT Creator

An AI-powered tool that generates YouTube video titles and scripts using OpenAI and Wikipedia research. This tool helps content creators streamline their video planning process by automatically generating engaging titles and well-researched scripts.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection for Wikipedia access

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your environment variables:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Run the application locally:

```bash
python -m streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Enter your topic or subject in the input field

4. Click "Generate" to create titles and scripts

## Features

- Generate catchy YouTube video titles based on topics
- Create detailed video scripts with Wikipedia research
- View and manage history of generated titles and scripts
- Access Wikipedia research used for content creation
- Export generated content in various formats

## Tech Stack

- Streamlit - Web interface
- LangChain - AI orchestration
- OpenAI - Content generation
- Wikipedia API - Research and fact-checking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have suggestions, please open an issue in the repository.
