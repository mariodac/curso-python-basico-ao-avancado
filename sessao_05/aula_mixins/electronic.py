from log import LogPrintMixin, LogFileMixin

class Electronic:
    def __init__(self, name) -> None:
        self._name = name
        self._status_power = False


    def start(self):
        if not self._status_power:
            self._status_power = True
        
    def shutdown(self):
        if self._status_power:
            self._status_power = False
# herança multipla tende a deixar o código complexo, prefira utilizar composição
class Smartphone(Electronic, LogFileMixin):

    def start(self):
        super().start()
        if self._status_power:
            msg = f'{self._name} está ligado'
            self.log_sucess(msg)

    def shutdown(self):
        super().shutdown()
        if not self._status_power:
            msg = f'{self._name} está desligado'
            self.log_error(msg)
