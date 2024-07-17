# Download driver https://googlechromelabs.github.io/chrome-for-testing/

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import openai
import time
import sys
import re
import os
from dotenv import load_dotenv

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'bin' / 'chromedriver.exe'
load_dotenv()
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_option = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_option.add_argument(option)
    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
    chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_option,)

    return chrome_browser


def ask_gpt(question:str, model_engine="davinci-002"):
    client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    try:
        completion = client.completions.create(model=model_engine, prompt=question,)
        print(completion.choices[0].text)
        print(dict(completion).get('usage'))
        print(completion.model_dump_json(indent=2))
    except Exception as err:
        _, _, tb = sys.exc_info()
        if tb is not None:
            print(f"Erro na linha {tb.tb_lineno} - {err}")
        else:
            print(f"Erro: {err}")


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    options = ('--disable-gpu', '--no-sandbox', )
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com/')

    # Esperar para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    try:
        search_terms = input('Digite o que será pesquisado -> ')
        search_input.send_keys(search_terms)
        search_input.send_keys(Keys.ENTER)

        results = browser.find_element(By.ID, 'search')
        links = results.find_elements(By.TAG_NAME, 'a')
        print('Os seguintes resultados foram encontrados: ')
        for index, link in enumerate(links):
            if len(link.text) > 1:
                print(f"{index+1} - {re.sub(r'\s{1,}', ' ', link.text)}")

        option = ''
        while type(option)  != int:
            option = input('Escolha a opção desejada: ')
            if option.isdigit():
                option = int(option)
                if option > 0 and option <= len(links):
                    if links:
                        links[option-1].click()
                        html_raw = BeautifulSoup(browser.page_source, 'html.parser')
                        ask_gpt(html_raw.text)
                    break
                else:
                    print('Opção inválida!')
            else:
                print('Opção inválida!')
    except Exception as err:
        _, _, tb = sys.exc_info()
        if tb is not None:
            print(f"Erro na linha {tb.tb_lineno} - {err}")
        else:
            print(f"Erro: {err}")
    time.sleep(TIME_TO_WAIT)
