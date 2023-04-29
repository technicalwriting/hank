source venv/bin/activate
export OPENAI_API_KEY=$(cat key.txt)
openai api fine_tunes.list
deactivate
