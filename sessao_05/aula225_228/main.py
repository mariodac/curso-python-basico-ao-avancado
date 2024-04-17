from log import Log, LogFileMixin, LogPrintMixin
from electronic import Smartphone

# lp = LogPrintMixin()
# lp.log_error('Qualquer coisa')
# lp.log_sucess('Que legal')
# lf = LogFileMixin()
# lf.log_error('Qualquer coisa')
# lf.log_sucess('Que legal')

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.start()
iphone.shutdown()