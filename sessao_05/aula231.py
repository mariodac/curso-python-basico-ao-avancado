# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes derivadas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatua do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação
# Sobrecarga de métodos (overload)      🐍 = ❌
# Sobreposição de métodos (override)    🐍 = ✅

from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def send(self) -> bool: ...

class NotificationEmail(Notification):

    def send(self) -> bool: 
        print('E-mail: enviando - ', self.msg)
        return False

class NotificationSms(Notification):

    def send(self) -> bool: 
        print('SMS: enviando - ', self.msg)
        return True

def notificate(notification: Notification):
    sent_notification = notification.send()

    if sent_notification:
        print('Notificação enviada com sucesso!')
    else:
        print('Não foi possível enviar a notificação!')

n = NotificationSms('testando')
n.send()
notificate(n)
notificate(NotificationEmail('Hello E-mail'))


