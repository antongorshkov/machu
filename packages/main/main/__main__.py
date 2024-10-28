import requests
def main(args):
  response = requests.get('https://zenquotes.io/api/random')
  data = response.json()[0]
  quote = data['q'] + ' - ' + data['a']
  return {
    'body': {
      'response_type': 'in_channel2',
      'text': quote
    }
  }
