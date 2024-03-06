from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
    loading = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=loading.get('url'), settings=settings)


def test_check_text(text):
    return client.service.checkText(text)[0]['s']


if __name__ == '__main__':
    print(test_check_text("Молако"))
