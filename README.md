# hank

A prototype to see if I can fine-tune an LLM into a style guide editor.

## Disclaimers & disclosures

Hello! This is Kayce Basques. I created this repository as a personal experiment.
I work for Google, but I did not seek out Google's approval to open source this
project and work on it publicly. Therefore this repository is not a Google product
"in any way, shape, or form." However, due to the terms of my employment with Google,
you should assume that Google could assert ownership over this repository if it wanted
to.

Also, hopefully it goes without saying, but just to be safe: if anything goes
wrong, then it's obviously 100% my fault and 0% Google's fault since I didn't seek
out Google's approval to work on this.

If any of this might be a problem for you, then please do not contribute to this
repository!

## Guidelines for contributing training data

The main thing that this experiment needs right now is more training data.
Contributing training data requires no programming knowledge.

### Pick a style guide rule

You can pick any style guide rule that you like, but please run it by me so
that I can:

* Make sure no one else is working on it
* Confirm that it will be easy to create training data for

The next few sections suggest some rules.

#### Suggestion: Present tense

* `Send a request to the server. The server will send JSON back.` (Before)
* `Send a request to the server. The server sends JSON back.` (After)

#### Suggestion: Second person

* `If we're deleting a database...` (Before)
* `If you're deleting a database...` (After)

### Create "before" and "after" examples

Create at least 25 examples of the style guide rule. Each example consists of
the original "before" text that contains the style guide violation and the "after"
text that contains the fixed text. The "before" and "after" text need to be identical
other than the style guide fix. Example:

* `Please click the button.` (Before)
* `Click the button.` (After)

#### Data formats

If you're comfortable with JSON, then this format is preferred:

```
[
  [
    "Please click the button.",
    "Click the button."
  ],
  ...
]
```

If you're not comfortable with JSON, then a CSV file would be fine. Or a spreadsheet.

#### Create text that is close to what you'd see in technical writing

The content of the writing doesn't have to strictly be about technical topics.
The writing style just needs to be close to what you'd see in a technical document.
Novel writing, for example, often has a very different style than technical writing.

#### Create multi-sentence, multi-paragraph, or complete-document examples

Each example should have a few sentences, at least. The style guide violation doesn't
have to be present in every sentence. For example, if you have a style guide rule
against using "please" in your docs, then this example would be fine:

```
Click the Submit button. Please wait for the order confirmation. If you click the
Back button, you may be charged twice.
```

(The first and last sentences have no problems. Only the middle sentence contains the violation.)

If you're comfortable with Markdown and using newline characters to represent new paragraphs
then it would be good to start training the LLM on examples like that because editing entire
Markdown docs is the long-term goal. For example:

```
# Hello, world!\n\nFirst paragraph.\n\n## How to make sushi\n\nSecond paragraph.
```

#### Create some GOTCHA examples

If there are any exceptions to the rule, create some examples that demonstrate those
exceptions, also. For example, suppose that you have a contractions rule. `It is` should
be edited to `It's`. However, think about the phrase `tell it like it is`. You wouldn't
edit this to `tell it like it's`! You capture the GOTCHA by creating an example where
the before and after are the same:

* `Tell it like it is.` (Before)
* `Tell it like it is.` (After)

## Why "hank"?

In honor of Hank "I Am The Bat" Venture.

![Henry Allen "Hank" Venture](www/hank.png)
