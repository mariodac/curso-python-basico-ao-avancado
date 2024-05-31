# locale para internacionalização
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar
import locale

# configurar locale do código
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print(locale.getlocale())

print(calendar.calendar(2022))

# exibe lista de todos locales do windows
for lang in locale.windows_locale.values():
    print(lang)
print()
for lang in locale.locale_alias.values():
    print(lang)