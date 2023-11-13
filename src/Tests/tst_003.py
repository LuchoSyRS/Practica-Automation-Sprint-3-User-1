from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

import pytest
from Pages.Bensimon_registro import Registro
from Pages import Bensimon_registro



class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver     


    def test_001(self):
        driver = self.driver
        driver.get("https://bensimon.com.ar/")
        time.sleep(3)
        pop_up = driver.find_element(By.ID, Registro.btn_popup_id)
        pop_up.click()
        time.sleep(3)
        
        driver.find_element(By.ID, Registro.dpd_dropdown_id).click()
        driver.find_element(By.XPATH, Registro.btn_CREAR_CUENTA_xpath).click()
        
        driver.find_element(By.ID, Registro.txt_Nombre_id).send_keys('Ricardo')
        driver.find_element(By.ID, Registro.txt_Apellido_id).send_keys('Perez')
        driver.find_element(By.ID, Registro.txt_Email_id).clear()
        driver.find_element(By.ID, Registro.txt_Email_id).send_keys("rictarj9090@gmail.com")
        driver.find_element(By.ID, Registro.txt_Contrasenia_id).clear()
        driver.find_element(By.ID, Registro.txt_Contrasenia_id).send_keys("pepe2222*")
        driver.find_element(By.ID, Registro.txt_Confirmar_la_contrasenia_id).send_keys("")
        driver.find_element(By.XPATH, Registro.btn_Registrarme_xpath).click()
        time.sleep(5)
        
        driver.find_element(By.ID, 'password-confirmation-error').is_displayed()

        time.sleep(5)
    
    def tearDown(self):  
        self.driver.close()
        
          
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()