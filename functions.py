import logging
import datetime
import os
import re
import traceback
from botcity.web import WebBot, Browser, By
from botcity.web.browsers.chrome import default_options
from botcity.maestro import *

def setup_logging():
    log_path = "C:/Users/ricar/Desktop/-/Compass/atividades-praticas-compass/Sprint-4/ativ-pratica-2-python-aa/resources/logfiles"
    # Verifica se a pasta "logfiles" existe, se não, cria-a
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo_log = f"{log_path}/logfile-{data_atual}.txt"

    logging.basicConfig(
        filename=nome_arquivo_log,
        level=logging.INFO,
        format="(%(asctime)s) - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S"
    )


def bot_driver_setup():
    bot = WebBot()
    def_options = default_options(
        headless = bot.headless,
        user_data_dir = r"C:\Users\ricar\AppData\Local\Google\Chrome\User Data"
    )

    bot.options = def_options
    bot.browser = Browser.CHROME
    bot.driver_path = r"C:\Users\ricar\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    return bot


def error_exception():
    error_msg = traceback.format_exc()  # Captura o erro com o traceback
    match = re.search(r'Message: (.*?)(?:\n|$)', error_msg)
    if match:
        error_msg = match.group(1).strip()
    logging.error(f"Erro: {error_msg}")
    return None
    

def browse_url(bot, url):
    return bot.browse(url)


def browse_close(bot):
    return bot.stop_browser()


def test_case_1(bot, url):
    logging.info("Inicio - Test case 1")
    browse_url(bot, url)
    add_btn = bot.find_element("#add_btn", By.CSS_SELECTOR)
    add_btn.click()
    logging.info("Clicado no botao 'add'.")
    try:
        # Verify Row 2 input field is displayed
        logging.info("Tenta capturar a linha 2.")
        row_2_field = bot.driver.find_element("css selector", "div[id='row2'] input[type='text']")
        row_2_field.send_keys("Baião de 2")

        logging.info("Campo row 2 preenchido.")
        browse_close(bot)
        return True
    except Exception:
        error_exception()
        browse_close(bot)
        return False


def test_case_2(bot, url):
    logging.info("Inicio - Test case 2")
    browse_url(bot, url)
    try:
        add_btn = bot.find_element("#add_btn", By.CSS_SELECTOR)
        add_btn.click()
        logging.info("Clicado no botao 'add'.")

        row_2_field = bot.find_element("div[id='row2'] input[type='text']", By.CSS_SELECTOR)
        row_2_field.send_keys("Baião de 2")
        logging.info("Linha 2 preenchida.")
        save_btn = bot.find_element("Save", By.NAME)
        save_btn.click()

        logging.info("Botao save clicado.")
        return True
    except Exception:
        error_exception()
        return False
    

def test_case_3(bot, url):
    logging.info("Inicio - Test case 3")
    browse_url(bot, url)
    try:
        row_1_field = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/div[1]/div[1]/div[1]/input[1]", By.XPATH)
        logging.info("Tentativa de dar clear() no campo.")
        row_1_field.clear()

        logging.info("Chegou aqui.")
        return True
    except Exception:
        error_exception()
        return False
    

def test_case_4(bot, url):
    logging.info("Inicio - Test case 4")
    browse_url(bot, url)
    try:
        instruction_element = bot.find_element("#instructions", By.CSS_SELECTOR)
        add_btn = bot.find_element("#add_btn", By.CSS_SELECTOR)
        add_btn.click()
        logging.info("Clicado no botao 'add'.")
        instruction_element.text

        logging.info(instruction_element.text)
        return True
    except Exception:
        error_exception()
        return False


def test_case_5(bot, url):
    logging.info("Inicio - Test case 5")
    browse_url(bot, url)
    try:
        add_btn = bot.find_element("#add_btn", By.CSS_SELECTOR)
        add_btn.click()

        bot.wait(3000)

        secont_input_field = bot.driver.find_element("css selector", "div[id='row2'] input[type='text']")

        return True
    except Exception:
        error_exception()
        return False