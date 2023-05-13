from glob import glob
from json import load
from os import getcwd
from jsonlines import open as jsonl_open
from sys import argv, exit

def get_config():
    cwd = getcwd()
    config_path = f'{cwd}/config.json'
    with open(config_path, 'r') as f:
        config = load(f)
    return config

def transform():
    out = []
    config = get_config()
    stop_sequence = config['stop_sequence']
    rules = config['rules']
    cwd = getcwd()
    for rule in rules:
        data_paths = glob(f'{cwd}/training/{rule}/*')
        data_paths.sort(reverse=True)
        for index, data_path in enumerate(data_paths):
            if index % 2 == 1:
                continue
            before_path = data_path
            with open(before_path, 'r') as f:
                before = f.read()
            after_path = data_paths[index + 1]
            with open(after_path, 'r') as f:
                after = f.read()
            input = f'{before}{stop_sequence}'
            # OpenAI output should start with a space:
            # https://platform.openai.com/docs/guides/fine-tuning/data-formatting
            output = f' {after}'
            out.append({'prompt': input, 'completion': output})
    with jsonl_open(f'{cwd}/training.jsonl', 'w') as jsonl_writer:
        jsonl_writer.write_all(out)

if __name__ == '__main__':
    try:
        if argv[1] == 'transform':
            transform()
        exit(0)
    except Exception as e:
        print(e)
        exit(1)