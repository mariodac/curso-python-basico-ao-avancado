# Empacotando a calculadora com PyInstaller


[Documentação pyinstaller](https://pyinstaller.org/en/stable/)

[Tutorial de Pythons GUIS](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/)

Instalação do pyinstaller

```python
pip install pyinstaller
```

Comando do pyinstaller no windows

```powershell
pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="sessao_07\aula_calculadora\files\;files\" --icon="sessao_07\aula_calculadora\files\icon.png" --noconsole --clean --log-level=WARN  .\sessao_07\aula_calculadora\main.py
```

Comando do pyinstaller no Mac/Linux

```powershell
pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="sessao_07/aula_calculadora/files:files/" --icon="sessao_07/aula_calculadora/files/icon.png" --noconsole --clean --log-level=WARN  sessao_07/aula_calculadora/main.py
```

Para personalizar a saída do pyinstaller

```powershell
pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="..\sessao_07\aula_calculadora\files\;files\" --icon="..\sessao_07\aula_calculadora\files\icon.png" --noconsole --clean --log-level=WARN --distpath ="output\dist" --workpath="output\build" --specpath="output\" .\sessao_07\aula_calculadora\main.py 
```

