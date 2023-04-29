source venv/bin/activate
if [ -z $1 ]; then
    echo 'Missing $1 (fine-tuning job ID)'
    deactivate
    return 1
fi
export OPENAI_API_KEY=$(cat key.txt)
openai api fine_tunes.follow -i $1
deactivate
