from urllib import request
import json
#"team-16|996141146944271"
default_api = "https://app-gateway.hackathon.ixaris.com/api"

def get_token(programmeID="996141146944271", credentialCode="team-16", password="1No2EXk&"):
  data = {
    "programmeId": programmeID,
    "credentialCode": credentialCode,
    "password": password
  }

  header = {
    "Content-Type": "application/json",
    "X-callref": password,
    "X-programmeKey": "{}|{}".format(credentialCode, programmeID),
  }

  req = request.Request(default_api + "/auth/login", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  token = json.loads(res.read().decode('utf-8'))

  header.update({"authorization": token['token']})

  with open('key.json', 'w') as f:
    f.write(str(header))

  return token

def issue_card(friendlyName, issuingProvider, processingProvider, nameOnCard, profileID="97593089101269248", ownerID="87593085012710413", currency="GBP"):
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {
    "profileId": profileID,
    "ownerId": ownerID,
    "friendlyName": friendlyName,
    "currency": currency,
    "issuingProvider": issuingProvider,
    "processingProvider": processingProvider,
    "nameOnCard": nameOnCard
  }

  req = request.Request(default_api + "/managed_cards/_/create", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  print(res.read())

def get_cards():
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {}

  req = request.Request(default_api + "/managed_cards/get", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  results = res.read()

  results = json.loads(results.decode('utf-8'))

  cards = results['cards']

  new_cardlist = []
  for card in cards:
    issuer = card['issuingProvider']
    if issuer == 'Halifax':
      card.update({'imageURL': 'https://github.com/jialutu/ixaris/blob/master/170125-halifax-clarity-card_d_1x.png?raw=true'})
    elif issuer == 'Barclays':
      card.update({'imageURL': 'https://github.com/jialutu/ixaris/blob/master/Credit_Card_BARCLAYCARD_INITIAL_FRONT_282x176.jpg?raw=true'})
    else:
      card.update({'imageURL': 'https://github.com/jialutu/ixaris/blob/master/bad-credit-merchant-account.jpg?raw=true'})

    new_cardlist.append(card)

  cards = {'cards': new_cardlist}

  return cards

def get_card(id):
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {}

  req = request.Request("{}/managed_cards/{}/get".format(default_api, id), data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  results = res.read()

  results = json.loads(results.decode('utf-8'))
  print(results)

  return results

def delete_card(id):
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {}

  req = request.Request("{}/managed_cards/{}/destroy".format(default_api, id), data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  results = res.read()

  results = json.loads(results.decode('utf-8'))
  print(results)

  return results

def create_corporation(name, support_email, notification_email):
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {
    "name": name,
    "profileId": "97593089101268736",
    "rootCredentialCode": "string",
    "supportEmail": support_email,
    "notificationEmail": notification_email,
    "adminTitle": "Mr",
    "adminName": "string",
    "adminSurname": "string",
    "adminEmail": "string"
  }

  req = request.Request(default_api + "/corporate_identities/_/create", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  print(res.read())

def get_corporations():
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {}

  req = request.Request(default_api + "/corporate_identities/get", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  results = res.read()

  results = json.loads(results.decode('utf-8'))

  return results

def create_accounts(name, support_email, notification_email):
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {
    "name": name,
    "profileId": "97593089101268736",
    "rootCredentialCode": "string",
    "supportEmail": support_email,
    "notificationEmail": notification_email,
    "adminTitle": "Mr",
    "adminName": "string",
    "adminSurname": "string",
    "adminEmail": "string"
  }

  req = request.Request(default_api + "/managed_accounts/_/create", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  print(res.read())

def get_accounts():
  with open('key.json', 'r') as f:
    header = f.read()
    header = json.loads(header.replace("'", '"'))

  data = {}

  req = request.Request(default_api + "/managed_accounts/profiles/get", data=str(data).encode('utf-8'), headers=header, method='POST')
  res = request.urlopen(req, timeout=5)

  results = res.read()

  results = json.loads(results.decode('utf-8'))

  return results

if __name__ == '__main__':
  #get_token()
  a = get_cards()
  #[print(i) for i in a if i['state'] == 'ACTIVE']
  print(str(a))