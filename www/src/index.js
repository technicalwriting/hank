export default {
  async fetch(request, env, ctx) {
    const url = 'https://api.openai.com/v1/chat/completions';
    const model = 'curie:ft-personal:hank-v2-2023-05-06-22-55-16';
    const requestOptions = {
      'method': 'POST',
      'headers': {
        'Content-Type': 'application/json',
        // https://developers.cloudflare.com/workers/platform/environment-variables/#add-secrets-to-your-project
        'Authorization': `Bearer ${env.OPENAI_API_KEY}`,
      },
      'body': JSON.stringify({
        'model': model,
        'messages': [{'role': 'user', 'content': 'Hello, world!'}],
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
