import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from models.robo_model import driver_chrome # --> func para driver rodar.
from models.robo_model import Acoes_Robo # --> class

from selenium import webdriver



def main():
    driver = webdriver.Chrome()
    robo = Acoes_Robo(driver=driver)
    with driver_chrome(driver=driver) as drive:
        drive.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        time.sleep(5)

        #Campo text --> Name, Email, Telefone, data_nasc.
        campo_input_name = robo.element((By.XPATH, '//*[@id="name"]'))
        campo_input_name_keys = robo.element_send_keys(locator=campo_input_name, text='Bob')

        campo_input_email = robo.element((By.XPATH, '//*[@id="email"]'))
        campo_input_email_keys = robo.element_send_keys(locator=campo_input_email, text='Bob@gmail.com')

        campo_input_telefone = robo.element((By.XPATH, '//*[@id="mobile"]'))
        campo_input_telefone_keys = robo.element_send_keys(campo_input_telefone, text='123456789')

        campo_input_data_nasc = robo.element((By.XPATH, '//*[@id="dob"]'))
        campo_input_data_nasc_keys = robo.element_send_keys(locator=campo_input_data_nasc, text='05042000')

        campo_input_current_address = robo.element((By.XPATH, '//textarea[@id="picture"]'))
        campo_input_current_address_keys = robo.element_send_keys(locator=campo_input_current_address, text='RuaOlavoMoura10-20')

        campo_input_subjects = robo.element((By.XPATH, '//*[@id="subjects"]'))
        campo_input_subjects_keys = robo.element_send_keys(locator=campo_input_subjects, text='blabla')

        #Campo CheckBox --> Genero, Hobbies.
        campo_check_genero = robo.element((By.XPATH, '//*[@id="gender"]'))
        campo_check_genero_click = robo.click_element(locator=campo_check_genero)

        campo_check_hobbies = robo.element((By.XPATH, '//*[@id="hobbies"]'))
        campo_check_hobbies_click = robo.click_element(locator=campo_check_genero)

        campo_upload = robo.element((By.XPATH, '//*[@id="picture"]'))
        campo_upload_keys = robo.element_send_keys(locator=campo_upload, text='C:/Users/Pichau/Downloads/Testes/Spider-Man Icon.jpg')

        #Campo Select -->
        select_element_site = robo.select_element((By.XPATH, '//*[@id="state"]'))
        print(select_element_site)

        text_element_select_state =  robo.select_by_visible_text(
            locator=(By.XPATH, '//*[@id="state"]'),
            text='NCR'
        )

        text_element_select_city = robo.select_by_visible_text(
            locator=(By.XPATH, '//*[@id="city"]'),
            text='Lucknow'
        )

        click_icon_select_state = robo.click_element(locator=text_element_select_state)
        click_icon_select_city = robo.click_element(locator=text_element_select_city)
        #Fim campo Select --!


        #Campo Button Login -->
        click_btn_login = robo.click_element((By.XPATH, '//*[@id="practiceForm"]/div[11]/input'))
        input('Espera --> ')
        time.sleep(2)

if  __name__ == '__main__':
    main()