**С использованием фреймворка pytest написать тест операции checkText
SOAP API https://speller.yandex.net/services/spellservice?WSDL
Тест должен использовать DDT и проверять наличие определенного
верного слова в списке предложенных исправлений к определенному
неверному слову.
Слова должны быть заданы через фикстуры в conftest.py,
адрес wsdl должен быть вынесен в config.yaml.
Методы работы с SOAP должны быть вынесены в отдельную библиотеку.**