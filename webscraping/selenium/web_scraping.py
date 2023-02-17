from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..models import Project
from decimal import Decimal
import datetime 
import json


def get_environmental_evaluation_projects():
    """Get information for enviromental evaluation projects."""
    url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    driver_path = './chromedriver.exe' # path to webdriver.exe in the system 
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    # initializate 
    driver.get(url)
    page_index = 1
    page_number = driver.find_element("xpath", f'//*[@id="info_resultado"]')
    pages_qty = int(page_number.text.split('\n')[-1].split(':')[1].replace(',',''))
    projects = []
    while page_index <= 10:
        for i in range(10):
            """Get project data from table."""
            id = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[1]')
            name = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[2]')
            project_type = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[3]')
            region = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[4]')
            typology = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[5]')
            titular = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[6]')
            investment = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[7]')
            date = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[8]')
            status = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[9]')
            map = ''
            try:
                map = driver.find_element("xpath", f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/table/tbody/tr[{i+1}]/td[10]/a')
                map = map.get_attribute('onclick').split("'")[1]
                map = 'https://seia.sea.gob.cl' + map
            except: 
                pass

            # Parse date and investment before create object.
            date = date.text.split('/')
            date_parsed = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
            investment = investment.text.replace('.','')
            # Create project object.
            project = Project.objects.create(
                project_id=int(id.text), name=name.text, project_type=project_type.text,
                region=region.text, typology=typology.text, titular=titular.text,
                investment=Decimal(investment.replace(',','.')), date=date_parsed, status=status.text, map=map
            )
            project.save()
            projects.append(project.serialize())
        page_index += 1
        # Change page
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/select')))\
            .click()
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div[1]/div/div[3]/div[4]/div/select/option[{page_index}]')))\
            .click()
    # Close driver
    driver.quit()
    return projects
                                      
def write_json(data, filename='projects.json'):
    """Create json file for projects data."""
    with open('mediafiles/projects_json/' + filename, "w") as f:
        json.dump(data, f, indent=2)