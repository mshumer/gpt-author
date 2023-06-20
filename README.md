# gpt-author

This project utilizes a chain of GPT-4 and Stable Diffusion API calls to generate an original fantasy novel. Users can provide an initial prompt and enter how many chapters they'd like it to be, and the AI then generates an entire novel, outputting an EPUB file compatible with e-book readers.

**A 15-chapter novel can cost as little as $4 to produce, and is written in just a few minutes.**

A few output novel examples are provided in this repo. To read one, you can download its file and view it on https://www.fviewer.com/view-epub, or install it on your Kindle, etc.

## How It Works

The AI is asked to generate a list of potential plots based on a given prompt. It then selects the most engaging plot, improves upon it, and extracts a title. After that, it generates a detailed storyline with a specified number of chapters, and then tries to improve upon that storyline. Each chapter is then individually written by the AI, following the plot and taking into account the content of previous chapters. Finally, a prompt to design the cover art is generated, and the cover is created. Finally, it's all pulled together, and the novel is compiled into an EPUB file.

## Usage

You can [run this project in Google Colab](https://colab.research.google.com/drive/1er_3U7lr6m4GJ-aHE6Pgeq9KXploxp4d?usp=sharing) or in a local Jupyter notebook. 

In Google Colab, simply open the notebook, add your API keys, and run the cells in order. 

If you are using a local Jupyter notebook, you will need to install the necessary dependencies. You can do this by running the following command in your terminal:

```bash
pip install openai ebooklib requests
```

In the last cell of the notebook, you can customize the prompt and the number of chapters for your novel. For example:

```python
prompt = "Similar to Percy Jackson or Harry Potter in terms of vibes, but a different plot entirely. Set in modern day. Add some element of technology to it."
num_chapters = 20
writing_style = "Clear and easily understandable, similar to a young adult novel. Highly descriptive and sometimes long-winded."
novel, title, chapters, chapter_titles = write_fantasy_novel(prompt, num_chapters, writing_style)
```

This will generate a novel based on the given prompt with 20 chapters. Note -- prompts with less than 7 chapters tend to cause issues.

## Contributions

Contributions, issues, and feature requests are welcome!

Some initial ideas:
- modify it to work solely with GPT-3.5-Turbo and GPT-3.5-Turbo-16k (it will likely require some level of compression/summariztion of early chapters so we don't run out of tokens when generating later chapters).
- improve the system for generating the first chapter -- the better the first chapter comes out, the better the rest of the novel is
- improve the prompts, as they were written very quickly
- improve each step in the process, adding more checks, improvement generations, etc.
- before generating improvements, have a model call identify potential improvements to add to the prompt, which will likely improve performance significantly
- modify it to go beyond just fantasy, allowing users to generate other genres as well
- fix the issue that causes some chapters to cut off early

## License

This project is [MIT](https://github.com/your_username/your_repository/blob/master/LICENSE) licensed.

## Contact

Matt Shumer - [@mattshumer_](https://twitter.com/mattshumer_)

Project Link: [https://github.com/mshumer/gpt-author/](https://github.com/mshumer/gpt-author/ )
