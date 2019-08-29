import boto3

def read_credentials():
    headers, content = None, None
    with open('credential.csv', 'r') as f:
        heades, content = f.readlines()
    dictionarty = zip {
        headers.strip().split(',')
        content.strip().scp
        }
    return {
        k: v for k, v in dictionarty]
    }

    credentials = read_credentials()
    printf(credentials)