"""
Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.
"""

from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from functions import *
import traceback

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    setup_logging()

    logging.info('Inicio - Atividade 2 - Python & Automation Anywhere')

    if execution.task_id == 0:
        logging.info("Maestro desativado -> Executando localmente")
        maestro = None

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = bot_driver_setup()

    url = "https://practicetestautomation.com/practice-test-exceptions/"


    case_1 = test_case_1(bot, url)
    if not case_1:
        logging.info("Foi gerado um erro.")
    else:
        logging.info("Concluido com sucesso.")
    logging.info("Fim - Test case 1")


    case_2 = test_case_2(bot, url)
    if not case_2:
        logging.info("Foi gerado um erro.")
    else:
        logging.info("Concluido com sucesso.")
    logging.info("Fim - Test case 2")


    case_3 = test_case_3(bot, url)
    if not case_3:
        logging.info("Foi gerado um erro.")
    else:
        logging.info("Concluido com sucesso.")
    logging.info("Fim - Test case 3")


    case_4 = test_case_4(bot, url)
    if not case_4:
        logging.info("Foi gerado um erro.")
    else:
        logging.info("Concluido com sucesso.")
    logging.info("Fim - Test case 4")

    case_5 = test_case_5(bot, url)
    if not case_5:
        logging.info("Foi gerado um erro.")
    else:
        logging.info("Concluido com sucesso.")
    logging.info("Fim - Test case 5")

    logging.info("Fim - Atividade 2 - Python & Automation Anywhere")


    if maestro:
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK.",
            total_items=0,
            processed_items=0,
            failed_items=0
        )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
