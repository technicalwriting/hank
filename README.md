# hank

Experimental code that attempts to fine-tune an LLM into a style guide editor.

See `//LOGS.md` for details about how the project is progressing.

Note: `//` means the root directory of this repository.

## Goals

The main goal is to speed up the process of editing text to follow a style guide.

The following H3 sections outline some sub-goals.

### Full-document editing

Ideally, I should be able to send a full document to the LLM and get back the
exact same document, edited for the style guide rules.

### GUI and API

I should be able to copy-paste the full document into some kind of GUI and
get back the edited document. I should also be able to `POST` the full document
to a web service API and get back the edited document in the response.

### Style guide rules customization

I should be able to pick-and-choose which style guide rules the fine-tuned LLM
is trained on.

### Model customization

I should be able to fine-tune LLMs from OpenAI, Google, etc.

## Licenses

Here are the licenses for the technical documents that were used as training data.

### developer.chrome.com

https://github.com/GoogleChrome/developer.chrome.com/blob/main/LICENSE

* [`//training/please/1_*.md`](https://github.com/GoogleChrome/developer.chrome.com/blob/e115dc46406bdc0667d6e614e6779f63ce52c8f8/site/en/docs/devtools/evaluate-performance/index.md)
* [`//training/please/2_*.md`](https://github.com/GoogleChrome/developer.chrome.com/blob/e115dc46406bdc0667d6e614e6779f63ce52c8f8/site/en/docs/devtools/css/index.md)