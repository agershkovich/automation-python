from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class UIInteractions:
    timeout = 10

    @staticmethod
    def waiting_for_element_visibility(driver, locator):
        return WebDriverWait(driver, UIInteractions.timeout).until(
            ec.visibility_of_element_located(locator))

    @staticmethod
    def waiting_for_element_is_clickable(driver, locator):
        return WebDriverWait(driver, UIInteractions.timeout).until(
            ec.element_to_be_clickable(locator))

    @staticmethod
    def click(driver, locator):
        UIInteractions.waiting_for_element_is_clickable(driver, locator).click()

    @staticmethod
    def input_text_value(driver, locator, value):
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(value)

    @staticmethod
    def input_issue_value(driver, locator, value):
        UIInteractions.waiting_for_element_is_clickable(driver, locator).click()
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(Keys.DELETE)
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(value)
        UIInteractions.waiting_for_element_visibility(driver, locator).send_keys(Keys.ENTER)

    @staticmethod
    def submit(driver, locator):
        UIInteractions.waiting_for_element_visibility(driver, locator).submit()

    @staticmethod
    def get_text(driver, locator):
        return UIInteractions.waiting_for_element_visibility(driver, locator).text

    @staticmethod
    def sing_sen_maker():
        s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie",
                   "This cool guy my gardener met yesterday", "Superman", 'Human Resources Manager', 'Accountant IV',
                   'Desktop Support Technician', 'General Manager', 'Actuary', 'Biostatistician III',
                   'Financial Analyst', 'Senior Cost Accountant', 'Civil Engineer', 'Marketing Assistant', 'Professor',
                   'GIS Technical Architect', 'Office Assistant I', 'Director of Sales', 'Operator',
                   'Associate Professor', 'Senior Editor', 'Tax Accountant', 'Help Desk Operator',
                   'Nuclear Power Engineer', 'Sales Associate', 'Actuary', 'Office Assistant I', 'Research Associate',
                   'Senior Sales Associate', 'Account Executive', 'Account Executive', 'VP Marketing', 'VP Sales',
                   'Human Resources Manager', 'Actuary', 'Administrative Assistant IV', 'Actuary', 'Social Worker',
                   'Chief Design Engineer', 'Graphic Designer', 'VP Marketing', 'Assistant Manager',
                   'Senior Cost Accountant', 'Administrative Assistant III', 'Software Test Engineer II',
                   'Human Resources Assistant IV', 'Dental Hygienist', 'Project Manager', 'Administrative Officer',
                   'Environmental Tech', 'Account Representative II', 'Associate Professor', 'Programmer Analyst III',
                   'Health Coach I', 'Research Associate', 'Administrative Assistant IV', 'Junior Executive',
                   'Registered Nurse', 'Office Assistant IV', 'Librarian', 'Librarian', 'Occupational Therapist',
                   'Financial Advisor', 'Senior Developer', 'Staff Accountant II', 'Speech Pathologist',
                   'Research Assistant IV', 'Accountant IV', 'VP Quality Control', 'Executive Secretary',
                   'Accounting Assistant III', 'Director of Sales', 'Research Assistant I',
                   'Human Resources Assistant III', 'Accountant II', 'Safety Technician I', 'Technical Writer',
                   'VP Marketing', 'Help Desk Operator', 'Senior Quality Engineer', 'Financial Analyst',
                   'Office Assistant IV', 'Programmer III', 'Help Desk Technician', 'Recruiting Manager',
                   'Human Resources Assistant I', 'Librarian', 'Dental Hygienist', 'General Manager',
                   'Staff Accountant I', 'Research Assistant III', 'Research Nurse', 'Paralegal', 'VP Marketing',
                   'Budget/Accounting Analyst IV', 'Help Desk Operator']

        p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys",
                   "All of a cattery's cats",
                   "The multitude of sloths living under your bed", "Your homies",
                   "Like, these, like, all these people"'Nycticorax nycticoraxs', 'Boa caninuss',
                   'Melanerpes erythrocephaluss', 'Lycosa godeffroyis', 'Manouria emyss', 'Macropus agiliss',
                   'Macropus agiliss', 'Bettongia penicillatas', 'Pteronura brasiliensiss', 'Boa caninuss',
                   'Phascogale caluras', 'Sitta canadensiss', 'Antechinus flavipess', 'Crotaphytus collariss',
                   'Chelodina longicolliss', 'Pelecans onocrataluss', 'Thamnolaea cinnmomeiventriss',
                   'Colaptes campestroidess', 'Turtur chalcospiloss', 'Milvus migranss', 'Priodontes maximuss',
                   'Echimys chrysuruss', 'Genetta genettas', 'Columba livias', 'Macropus rufogriseuss',
                   'Eumetopias jubatuss', 'Aonyx cinereas', 'Corvus albicolliss', 'Anas punctatas', 'Struthio cameluss',
                   'Centrocercus urophasianuss', 'Phasianus colchicuss', 'Nyctanassa violaceas', 'Lutra canadensiss',
                   'Crotalus cerastess', 'Branta canadensiss', 'Larus novaehollandiaes', 'Phoenicopterus rubers',
                   'Equus burchellis', 'Melanerpes erythrocephaluss', 'Papio cynocephaluss', 'Caiman crocodiluss',
                   'Taxidea taxuss', 'Eubalaena australiss', 'Alopochen aegyptiacuss', 'Colobus guerzas',
                   'Tamiasciurus hudsonicuss', 'Deroptyus accipitrinuss', 'Pteronura brasiliensiss',
                   'Columba palumbuss', 'Pseudocheirus peregrinuss', 'Bubo virginianuss', 'unavailables',
                   'Phalaropus fulicariuss', 'Ovis ammons', 'Ctenophorus ornatuss', 'Mellivora capensiss',
                   'Marmota flaviventriss', 'Eurocephalus anguitimenss', 'Ninox superciliariss',
                   'Lamprotornis chalybaeuss', 'Dasyurus maculatuss', 'Elephas maximus bengalensiss',
                   'Dicrostonyx groenlandicuss', 'Varanus sp.s', 'Carduelis pinuss', 'Odocoileus hemionuss',
                   'Cygnus buccinators', 'Corvus brachyrhynchoss', 'Bubo sp.s', 'Ceratotherium simums',
                   'Alectura lathamis', 'Ursus americanuss', 'Bugeranus caruncalatuss', 'Uraeginthus granatinas',
                   'Naja hajes', 'Arctogalidia trivirgatas', 'Gorilla gorillas', 'Dasypus novemcinctuss',
                   'Graspus graspuss', 'Vombatus ursinuss', 'Pycnonotus nigricanss', 'Felis wiedi or Leopardus weidis',
                   'Lama guanicoes', 'Lasiorhinus latifronss', 'Cygnus atratuss', 'Francolinus swainsoniis',
                   'Boa constrictor mexicanas', 'Eumetopias jubatuss', 'Anas punctatas', 'Chlidonias leucopteruss',
                   'Pytilia melbas', 'Phoca vitulinas', 'Platalea leucordias', 'Mycteria leucocephalas',
                   'Chlidonias leucopteruss', 'Hyaena hyaenas', 'Phoenicopterus chilensiss', 'Felis yagouaroundis',
                   'Grus rubicunduss']

        s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on",
                   "retards", "meows on", "flees from", "tries to automate", "explodes"]
        p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard",
                   "meow on", "flee from", "try to automate", "explode"]
        infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.",
                       "to be able to make toast explode.", "to know more about archeology."]

        import random

        return (random.choice(s_nouns) + " " + random.choice(s_verbs) + " " + random.choice(
            s_nouns).lower() or random.choice(
            p_nouns).lower() + " " + random.choice(p_verbs) + " " + random.choice(infinitives))
