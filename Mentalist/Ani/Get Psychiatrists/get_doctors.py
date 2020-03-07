from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.options import Options 
import itertools
import random
start_phone = [''.join(x) for x in list(itertools.permutations('899',3))]

def get_doctors(place):
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)

    driver.get('https://www.practo.com/')

    # For Searching for the locality
    locality_input_element = driver.find_element_by_xpath('//input[@data-qa-id="omni-searchbox-locality"]')

    locality_input_element.send_keys(Keys.CONTROL + "a")
    locality_input_element.send_keys(Keys.DELETE)

    locality_input_element.send_keys(place)

    sleep(1)

    suggestion = driver.find_element_by_xpath('//div[@class="c-omni-suggestion-group"][1]/div[1]')

    suggestion.click()

    sleep(1)

    # For Searching the type of doctor

    doctor_input_element = driver.find_element_by_xpath('//input[@data-qa-id="omni-searchbox-keyword"]')

    doctor_input_element.send_keys('Psychiatrist')

    sleep(2)

    suggestion = driver.find_element_by_xpath('//div[@class="c-omni-suggestion-group"][1]/div[1]')

    suggestion.click()

    doctor_details = []

    doctors_list = driver.find_elements_by_xpath('//div[@class="info-section"]')

    doctor_phones = [random.choice(start_phone)+str(random.getrandbits(26)) for _ in range(len(doctors_list))]

    for doctor, phone in zip(doctors_list, doctor_phones):

        name = doctor.find_element_by_xpath('.//h2[@class="doctor-name"]').text

        experience = doctor.find_element_by_xpath('.//div[1]/div[2]/div').text
        
        consultation_fee = doctor.find_element_by_xpath('.//span[@data-qa-id="consultation_fee"]').text

        doctor_details.append({
            'Name': name,
            'Phone': phone,
            'Experience': experience,
            'Consultation_fee': consultation_fee
        })

    return(doctor_details)

if __name__ == '__main__':
    print(get_doctors('Vileparle')) 
    