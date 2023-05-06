import jsonlines

data = [
    {
        "original": "It is possible to fine-tune an LLM to enforce a style guide.",
        "edited": "It's possible to fine-tune an LLM to enforce a style guide."
    },
    {
        "original": "It is raining men, hallelujah",
        "edited": "It's raining men, hallelujah"
    },
    {
        "original": "I think it is Travis.",
        "edited": "I think it's Travis."
    },
    {
        "original": "I can't believe it is not butter!",
        "edited": "I can't believe it's not butter!"
    },
    {
        "original": "The problem is that it is a complicated sentence.",
        "edited": "The problem is that it's a complicated sentence."
    },
    {
        "original": "I don't know what it is.",
        "edited": "I don't know what it is."
    },
    {
        "original": "It is never too late to learn.",
        "edited": "It's never too late to learn."
    },
    {
        "original": "I like it as it is.",
        "edited": "I like it as it is."
    },
    {
        "original": "Maybe it is going to rain?",
        "edited": "Maybe it's going to rain?"
    },
    {
        "original": "It is normal to feel that way.",
        "edited": "It's normal to feel that way."
    },
    {
        "original": "Please click the button.",
        "edited": "Click the button."
    },
    {
        "original": "To run the job, please select Go.",
        "edited": "To run the job, select Go."
    },
    {
        "original": "Please enter your username.",
        "edited": "Enter your username."
    },
    {
        "original": "Please note that the feature is now generally available.",
        "edited": "Note that the feature is now generally available."
    },
    {
        "original": "For more information, please see the FAQ.",
        "edited": "For more information, see the FAQ."
    },
    {
        "original": "Please configure the app to run on HTTPS only.",
        "edited": "Configure the app to run on HTTPS only."
    },
    {
        "original": "To learn how to change a tire, please see the owner's manual.",
        "edited": "To learn how to change a tire, see the owner's manual."
    },
    {
        "original": "Listen to the voicemail, please.",
        "edited": "Listen to the voicemail."
    },
    {
        "original": "Open the menu and then please select your country.",
        "edited": "Open the menu and then select your country."
    },
    {
        "original": "Please wait for the tryjob to finish.",
        "edited": "Wait for the tryjob to finish."
    }
]

output = []

for item in data:
    original = item['original']
    edited = item['edited']
    prompt = 'FIXME: {}@STOP!!'.format(original)
    completion = ' {}'.format(edited)
    output.append({'prompt': prompt, 'completion': completion})
    with jsonlines.open('training.jsonl', 'w') as writer:
        writer.write_all(output)
