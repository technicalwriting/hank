source venv/bin/activate
if [ -z $1 ]; then
    echo 'Missing $1 (model name suffix)'
    deactivate
    return 1
fi
export OPENAI_API_KEY=$(cat key.txt)
python3 transform.py
openai api fine_tunes.create -t training.jsonl -m ada --suffix $1
deactivate
