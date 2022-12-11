import re
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from lib2to3.pgen2 import driver

class FunctionnalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # cls.options.add_argument('--headless')
        cls.browser = webdriver.Chrome(executable_path=r"C:\Users\lebas\Documents\IUT L3\chromedriver.exe")
        cls.browser.implicitly_wait(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        super().tearDownClass()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_unauthenticated_all

    def test_unauthenticated_all(self):
        """Test when if user isn't authenticated, he hasn't acces to forms etc."""
        # va a l'url
        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")
        time.sleep(0.2)
        # recherche s'il y a un button sur la page
        button = self.browser.find_elements(By.TAG_NAME, "button")
        # check si il y a 0 boutton (car find_elements retourne un tableau de tout les elements qu'il toruve)
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/motherBoard/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/processeur/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/gpu/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/ram/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/stockage/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])


    # ./manage.py test pcMaker.tests.FunctionnalTest.test_connexion    
    def test_connexion(self, pseudo="alexis", mdp="Alexis1234@#"):
        """Connexion with a user"""

        self.browser.get("http://127.0.0.1:8000/pcMaker/")

        time.sleep(0.5)

        self.browser.find_element(By.XPATH, "//*[contains(text(), 'Se connecter')]").click()

        time.sleep(0.5)

        self.browser.find_element(By.ID, "id_username").send_keys(pseudo)
        self.browser.find_element(By.ID, "id_password").send_keys(mdp)

        self.browser.find_element(By.CSS_SELECTOR, "input[value*='login']").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_deco  
    def test_deco(self):
        self.browser.get("http://127.0.0.1:8000/pcMaker/")
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//*[contains(text(), 'Se déconnecter')]").click()

    def test_authenticated_build_pc(self):

        self.test_connexion()
        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")

        self.browser.find_element(By.ID, "id_alimentation").send_keys(800)
        self.browser.find_element(By.ID, "id_gpu").click()
        time.sleep(2)
        select = Select(self.browser.find_element(By.ID, "id_gpu"))
        select.select_by_value("1")


    # ./manage.py test pcMaker.tests.FunctionnalTest.test_authenticated_all
    def test_authenticated_all(self):

        self.test_connexion()

        self.browser.get("http://127.0.0.1:8000/pcMaker/motherBoard/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/processeur/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/gpu/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/ram/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/stockage/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_admin_all
    def test_admin_all(self):

        self.test_connexion("admin", "admin")

        self.browser.get("http://127.0.0.1:8000/pcMaker/motherBoard/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/processeur/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/gpu/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/ram/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/stockage/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])

        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")
        time.sleep(0.2)
        button = self.browser.find_elements(By.TAG_NAME, "button")
        self.assertNotEqual(button, [])


##########################################  MOTHERBOARD  ################################################


    # ./manage.py test pcMaker.tests.FunctionnalTest.test_add_mb
    def test_add_mb(self):

        self.test_connexion("admin", "admin")
        marque = "ASUS"
        chipset = "B660"
        self.browser.get("http://127.0.0.1:8000/pcMaker/motherBoard/")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "id_marque").send_keys(marque)
        self.browser.find_element(By.ID, "id_chipset").send_keys(chipset)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    
    # ./manage.py test pcMaker.tests.FunctionnalTest.test_del_mb
    def test_del_mb(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/motherBoard/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[3]/a/button").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_edit_mb
    def test_edit_mb(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/motherBoard/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[4]/a/button").click()
        self.browser.find_element(By.ID, "id_marque").clear()
        self.browser.find_element(By.ID, "id_marque").send_keys("MSI")
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_all_mb
    def test_all_mb(self):
        self.test_add_mb()
        self.test_deco()
        self.test_edit_mb()
        self.test_deco()
        self.test_del_mb()


##########################################  PROCESSEUR  ################################################


    # ./manage.py test pcMaker.tests.FunctionnalTest.test_add_cpu
    def test_add_cpu(self):

        self.test_connexion("admin", "admin")
        marque = "Intel"
        cat = "i9"
        modele = "13900k"
        self.browser.get("http://127.0.0.1:8000/pcMaker/processeur/")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "id_marque").send_keys(marque)
        self.browser.find_element(By.ID, "id_categorie").send_keys(cat)
        self.browser.find_element(By.ID, "id_modele").send_keys(modele)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_edit_cpu
    def test_edit_cpu(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/processeur/")
        time.sleep(0.2)
        nbtb = self.browser.find_elements(By.TAG_NAME, "tbody")
        lastline = len(nbtb)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[5]/a/button").click()
        self.browser.find_element(By.ID, "id_marque").clear()
        self.browser.find_element(By.ID, "id_marque").send_keys("Ryzen")
        self.browser.find_element(By.ID, "id_categorie").clear()
        self.browser.find_element(By.ID, "id_categorie").send_keys("R9")
        self.browser.find_element(By.ID, "id_modele").clear()
        self.browser.find_element(By.ID, "id_modele").send_keys("5950X")
        self.browser.find_element(By.ID, "submit").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_del_cpu
    def test_del_cpu(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/processeur/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[4]/a/button").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_all_cpu
    def test_all_cpu(self):
        self.test_add_cpu()
        self.test_deco()
        self.test_edit_cpu()
        self.test_deco()
        self.test_del_cpu()

##########################################  CRATE GRAPHIQUE  ################################################

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_add_gpu
    def test_add_gpu(self):

        self.test_connexion("admin", "admin")
        marque = "Nvidia"
        modele = "RTX 3090Ti"
        self.browser.get("http://127.0.0.1:8000/pcMaker/gpu/")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "id_marque").send_keys(marque)
        self.browser.find_element(By.ID, "id_modele").send_keys(modele)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_edit_gpu
    def test_edit_gpu(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/gpu/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[4]/a/button").click()
        self.browser.find_element(By.ID, "id_marque").clear()
        self.browser.find_element(By.ID, "id_marque").send_keys("AMD")
        self.browser.find_element(By.ID, "id_modele").clear()
        self.browser.find_element(By.ID, "id_modele").send_keys("RX 6800XT")
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_del_gpu
    def test_del_gpu(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/gpu/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[3]/a/button").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_all_gpu
    def test_all_gpu(self):
        self.test_add_gpu()
        self.test_deco()
        self.test_edit_gpu()
        self.test_deco()
        self.test_del_gpu()


##########################################  RAM  ################################################

# ./manage.py test pcMaker.tests.FunctionnalTest.test_add_ram
    def test_add_ram(self):

        self.test_connexion("admin", "admin")
        marque = "HyperX"
        freq = 3800
        taille = 16
        self.browser.get("http://127.0.0.1:8000/pcMaker/ram/")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "id_marque").send_keys(marque)
        self.browser.find_element(By.ID, "id_frequence").send_keys(freq)
        self.browser.find_element(By.ID, "id_taille").send_keys(taille)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    
    # ./manage.py test pcMaker.tests.FunctionnalTest.test_del_ram
    def test_del_ram(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/ram/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[4]/a/button").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_edit_ram
    def test_edit_ram(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/ram/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        time.sleep(0.2)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[5]/a/button").click()
        self.browser.find_element(By.ID, "id_marque").clear()
        self.browser.find_element(By.ID, "id_marque").send_keys("Kingston")
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_all_ram
    def test_all_ram(self):
        self.test_add_ram()
        self.test_deco()
        self.test_edit_ram()
        self.test_deco()
        self.test_del_ram()

##########################################  STOCKAGE  ################################################

# ./manage.py test pcMaker.tests.FunctionnalTest.test_add_stockage
    def test_add_stockage(self):

        self.test_connexion("admin", "admin")
        type = "HDD"
        taille = 4000
        self.browser.get("http://127.0.0.1:8000/pcMaker/stockage/")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "id_type").send_keys(type)
        self.browser.find_element(By.ID, "id_taille").send_keys(taille)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    
    # ./manage.py test pcMaker.tests.FunctionnalTest.test_del_stockage
    def test_del_stockage(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/stockage/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[3]/a/button").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_edit_stockage
    def test_edit_stockage(self):

        self.test_connexion("admin", "admin")
        self.browser.get("http://127.0.0.1:8000/pcMaker/stockage/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        time.sleep(0.2)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[4]/a/button").click()
        self.browser.find_element(By.ID, "id_type").clear()
        self.browser.find_element(By.ID, "id_type").send_keys("M.2")
        self.browser.find_element(By.ID, "id_taille").clear()
        self.browser.find_element(By.ID, "id_taille").send_keys("500")
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_all_stockage
    def test_all_stockage(self):
        self.test_add_stockage()
        self.test_deco()
        self.test_edit_stockage()
        self.test_deco()
        self.test_del_stockage()

##########################################  ORDINATEUR  ################################################

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_add_pc
    def test_add_pc(self):

        self.test_connexion()
        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")
        time.sleep(1)
        self.browser.find_element(By.ID, "id_alimentation").send_keys(1200)
        self.browser.find_element(By.ID, "id_gpu").click()
        select = Select(self.browser.find_element(By.ID, "id_gpu"))
        select.select_by_index(1)
        select = Select(self.browser.find_element(By.ID, "id_stockage"))
        select.select_by_index(1)
        time.sleep(0.5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        self.browser.find_element(By.ID, "id_processeur").click()
        select = Select(self.browser.find_element(By.ID, "id_processeur"))
        select.select_by_index(1)
        self.browser.find_element(By.ID, "id_ram").click()
        select = Select(self.browser.find_element(By.ID, "id_ram"))
        select.select_by_index(1)
        self.browser.find_element(By.ID, "id_motherBoard").click()
        select = Select(self.browser.find_element(By.ID, "id_motherBoard"))
        select.select_by_index(1)
        self.browser.find_element(By.ID, "submit").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_del_pc
    def test_del_pc(self):

        self.test_connexion()
        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[8]/a/button").click()

    # ./manage.py test pcMaker.tests.FunctionnalTest.test_edit_pc
    def test_edit_pc(self):

        self.test_connexion()
        self.browser.get("http://127.0.0.1:8000/pcMaker/ordinateur/")
        time.sleep(0.2)
        nbtr = self.browser.find_elements(By.TAG_NAME, "tr")
        lastline = len(nbtr)
        time.sleep(0.2)
        self.browser.find_element(By.XPATH, "/html/body/main/div/table/tbody["+str(lastline-1)+"]/tr/td[9]/a/button").click()
        self.browser.find_element(By.ID, "id_alimentation").clear()
        self.browser.find_element(By.ID, "id_alimentation").send_keys(1100)
        self.browser.find_element(By.ID, "id_motherBoard").click()
        select = Select(self.browser.find_element(By.ID, "id_motherBoard"))
        select.select_by_index(2)
        self.browser.find_element(By.ID, "submit").click()
        time.sleep(0.2)

     # ./manage.py test pcMaker.tests.FunctionnalTest.test_all_pc
    def test_all_pc(self):
        self.test_add_pc()
        self.test_deco()
        self.test_edit_pc()
        self.test_deco()
        self.test_del_pc()
