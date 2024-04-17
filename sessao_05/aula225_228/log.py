# Abstração
# Herança - é um
from pathlib import Path

# o / concatena de acordo com o tipo de sistema
LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    
class LogFileMixin(Log):
    # para sobrepor um método deve ter a mesma assinatura
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_format)
        with open(LOG_FILE, 'a', encoding='utf-8') as file_log:
            file_log.write(msg_format)
            file_log.write('\n')

class LogPrintMixin(Log):
    # para sobrepor um método deve ter a mesma assinatura
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_sucess('Que legal')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_sucess('Que legal')