export default {
  async fetch(request, env, ctx) {
    const url = 'https://api.openai.com/v1/completions';
    const model = 'curie:ft-personal:hank-v3-2023-05-06-23-41-12';
    const stopSequence = 'KEEP CIRCULATING THE TAPES';
    const requestOptions = {
      'method': 'POST',
      'headers': {
        'Content-Type': 'application/json',
        // https://developers.cloudflare.com/workers/platform/environment-variables/#add-secrets-to-your-project
        'Authorization': `Bearer ${env.OPENAI_API_KEY}`,
      },
      'body': JSON.stringify({
	'prompt': `Please do not touch it. It is not a toy.${stopSequence}`,
        'model': model,
        'temperature': 0,
      }),
    };
    const response = await fetch(url, requestOptions);
    const json = await response.json();
    const responseOptions = {
      'headers': {
        'content-type': 'application/json',
      },
    };
    return new Response(JSON.stringify(json), responseOptions);
  },
};
