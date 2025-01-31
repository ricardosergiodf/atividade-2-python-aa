# Automacao de Login com Python e BotCity

## Descricao
Este projeto tem como objetivo a captura de erros ao interagir com a pagina [Practice Test Automation](https://practicetestautomation.com/practice-test-exceptions/) utilizando Python e BotCity. A aplicacao executa diferentes casos de teste para validar a interacao com elementos da interface, capturando excecoes especificas e gerando logs detalhados.

## Tecnologias Utilizadas
- **Python**
- **BotCity** (Automacao Web)
- **Selenium WebDriver**
- **Logging** (Captura de logs)

## Estrutura do Projeto
```
/
|-- bot.py               # Script principal para execucao dos testes
|-- functions.py         # Funcoes auxiliares para interacao com a web
|-- requirements.txt     # Dependencias do projeto
|-- resources/
    |-- logfiles/        # Arquivos de log gerados durante a execucao
```

## Instalacao
1. Clone este repositorio:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependencias:
   ```bash
   pip install --upgrade -r requirements.txt
   ```
3. Certifique-se de que o **ChromeDriver** esta instalado e configurado corretamente no caminho definido em `functions.py`.

## Como Executar
Para rodar o bot, basta executar:
```bash
python bot.py
```
Se estiver utilizando o Automation Anywhere Maestro, o bot podera ser gerenciado remotamente.

## Test Cases Implementados
O projeto executa 5 casos de teste distintos, cada um visando capturar um erro especifico:

1. **Test Case 1: NoSuchElementException**
   - Abrir a pagina
   - Clicar no botao "Add"
   - Verificar se o campo de entrada da linha 2 e exibido
   - **Erro esperado:** `NoSuchElementException`, pois a linha 2 nao aparece imediatamente

2. **Test Case 2: ElementNotInteractableException**
   - Abrir a pagina
   - Clicar no botao "Add"
   - Aguardar a segunda linha carregar
   - Digitar texto no segundo campo de entrada
   - Clicar no botao "Save" usando `By.name("Save")`
   - **Erro esperado:** `ElementNotInteractableException`, pois ha dois elementos com `name="Save"`, sendo o primeiro invisivel

3. **Test Case 3: InvalidElementStateException**
   - Abrir a pagina
   - Tentar limpar um campo de entrada desativado
   - Digitar texto no campo
   - **Erro esperado:** `InvalidElementStateException`, pois o campo e desativado e precisa ser ativado antes da edicao

4. **Test Case 4: StaleElementReferenceException**
   - Abrir a pagina
   - Encontrar o elemento de texto "instructions"
   - Clicar no botao "Add"
   - Verificar se o elemento "instructions" ainda esta disponivel
   - **Erro esperado:** `StaleElementReferenceException`, pois o elemento e removido da pagina ao adicionar a segunda linha

5. **Test Case 5: TimeoutException**
   - Abrir a pagina
   - Clicar no botao "Add"
   - Aguardar 3 segundos pela exibicao do segundo campo de entrada
   - **Erro esperado:** `TimeoutException`, pois a segunda linha aparece apenas apos 5 segundos

Cada teste captura logs detalhados e, em caso de falha, os erros sao registrados.

## Logs
Os logs sao gerados automaticamente na pasta:
```
resources/logfiles/logfile-YYYY-MM-DD_HH-MM-SS.txt
```
Eles contem informacoes sobre cada execucao, erros encontrados e tempo de execucao.

## Contribuicao
Caso queira contribuir com melhorias, sinta-se livre para abrir um pull request ou relatar problemas na aba de **Issues**.

## Licença
Este projeto esta sob a licença MIT. Voce pode usar, modificar e distribuir livremente.

