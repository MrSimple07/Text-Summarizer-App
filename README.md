# Text Summarization App

This is a simple app that uses the `facebook/bart-large-cnn` model from Hugging Face to summarize long-form text. The app takes an article, paper, or book, and summarizes it into key points or a concise paragraph.

## Features

- Summarizes long text into a short, readable summary.
- Works on various kinds of text (articles, papers, books).
- Uses Hugging Face's BART model for high-quality summaries.
- Provides a simple and user-friendly interface built with Gradio.

## How It Works

1. The user inputs a long-form text (article, paper, or book) in the provided input box.
2. The app processes the input using the `facebook/bart-large-cnn` model.
3. A summarized version of the text is displayed as output.

## Technologies Used

- **Gradio**: For the user interface.
- **Hugging Face Transformers**: For using the pre-trained BART model for summarization.
- **PyTorch**: Deep learning framework used for running the BART model.

## Example

Input: "Long article text here..."

Output: "Concise summary of the article here..."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You can check it here: https://huggingface.co/spaces/MrSimple07/Text_summarizer/

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
