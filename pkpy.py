# -*- coding: utf-8 -*-

import requests
import time
import re
import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

WebDriverPath = "chromedriver.exe"

makeHeadles = webdriver.ChromeOptions()
makeHeadles.add_argument('headless')
makeHeadles.add_experimental_option('excludeSwitches', ['enable-logging'])
SeleniumDriver = webdriver.Chrome(options=makeHeadles)

czas = time.localtime()
current_time = time.strftime("%H:%M:%S", czas)
aktualna_data = datetime.today().strftime('%d/%m/%Y')
data_payload = datetime.today().strftime('%d%m%Y')
current_time_payload = time.strftime("%H%M", czas)
czas_payload = data_payload + current_time_payload

zegarek_data = datetime.today().strftime('%d/%m/%Y')
zegarek_czas = time.strftime("%H:%M", czas)

print("\n")
print(f"   PKPython 1.0                                   Czas 🢒  {zegarek_data} [{zegarek_czas}]  ")
print("\n")
print("\033[0;37;40m     ____  ____  ____  ____   ____ ____ ____ ____   ____  ____  ____  ___   \033[0;37;40m")
print("\033[0;37;40m    ||  ||||  ||||  ||||  || ||P |||K |||P |||y || ||  ||||  ||||  ||||  \   \033[0;37;40m")
print("\033[0;37;40m    ||__||||__||||__||||__||-||__|||__|||__|||__||-||__||||__||||__||||__ C   \033[0;37;40m")
print("\033[1;31;40m    |/__\||/__\||/__\||/__\| |/__\|/__\|/__\|/__\| |/__\||/__\||/__\||/__\|   \033[0;37;40m")
print("\033[1;31;40m                                                                             \033[0;37;40m")
print("\n")
print("   [PUBLIC BETA]                                    Mikołaj Połonowicz ©2022")
print("\n")

print("Ładowanie Stacji... ↻")
print("\n")
stations_list = WordCompleter(['Andrychów', 'Anieliny', 'Babimost', 'Baborówko', 'Balinka', 'Bardo Przyłęk', 'Bardo Śląskie', 'Barłogi', 'Bełchów', 'Będzin Miasto', 'Biadoliny', 'Biała Podlaska', 'Białogard', 'Białośliwie', 'Biały Bór', 'Biały Dunajec', 'Białystok', 'Białystok Bacieczki', 'Bielsk Podlaski', 'Bielsko-Biała Główna', 'Bierutów', 'Bierzwnik', 'Bińcze', 'Biskupice Wielkopolskie', 'Biskupiec Pomorski', 'Błądzim', 'Błonie', 'Bochnia', 'Boguszów Gorce Zachód', 'Bojanowo', 'Bolesławiec', 'Boleszkowice', 'Boronów', 'Borowa Oleśnicka', 'Braniewo', 'Bronów', 'Brusy', 'Brwinów', 'Brzeg', 'Brzeg Dolny', 'Brzesko Okocim', 'Budachów', 'Budzyń', 'Bukowo', 'Bydgoszcz Główna', 'Bydgoszcz Łęgnowo', 'Bystrzyca Kłodzka Przedmieście', 'Bytom', 'Bytom Odrzański', 'Cekcyn', 'Celestynów', 'Chełm', 'Chełm Miasto', 'Chocicza', 'Chociwel', 'Chodzież', 'Chojna', 'Chojnów', 'Chorzów Batory', 'Chrząstowice', 'Chynów', 'Ciechanów', 'Czaplinek', 'Czarna Białostocka', 'Czarna Tarnowska', 'Czarna Woda', 'Czechowice Dziedzice', 'Czempiń', 'Czeremcha', 'Czerwieńsk', 'Czerwonka', 'Częstochowa', 'Częstochowa Stradom', 'Czyżew', 'Damnica', 'Dąbrowa Białostocka', 'Dęba Opoczyńska', 'Dębe Wielkie', 'Dębica', 'Dęblin', 'Dobieszyn', 'Dobroszyce', 'Dolice', 'Domaszków', 'Drawski Młyn', 'Duszniki-Zdrój', 'Działdowo', 'Dziembówko', 'Dziemiany Kaszubskie', 'Dziewule', 'Elbląg', 'Ełk', 'Gałkówek', 'Garbatka Letnisko', 'Gądki', 'Gądków Wielki', 'Gdańsk Główny', 'Gdańsk Oliwa', 'Gdańsk Osowa', 'Gdańsk Wrzeszcz', 'Gdynia Chylonia', 'Gdynia Główna Osobowa', 'Giżycko', 'Gliwice', 'Głogów', 'Głogówek', 'Głowno', 'Głuchołazy', 'Głuszyca', 'Gniewkowo', 'Gniezno', 'Gołubie Kaszubskie', 'Gorzanów', 'Gorzkowice', 'Gorzów Wielkopolski', 'Grabów nad Pilicą', 'Granowiec', 'Gręboszów', 'Grodzisk Mazowiecki', 'Grudziądz', 'Grupa', 'Gryfice', 'Gryfino', 'Grzmiąca', 'Hel', 'Iława Główna', 'Iłowiec', 'Imbramowice', 'Inowrocław', 'Iwin', 'Jabłonowo Pomorskie', 'Jabłoń Kościelna', 'Jaktorów', 'Janikowo', 'Janinów', 'Jarocin', 'Jarosław', 'Jasienica Mazowiecka', 'Jasień Brzeski', 'Jastrowie', 'Jastrzębna', 'Jawor', 'Jaworzyna Śląska', 'Jelenia Góra', 'Jeżewo', 'Jędrzejów', 'Józefów', 'Kaliska', 'Kaliska Kujawskie', 'Kalisz', 'Kalisz Kaszubski', 'Kamieniec Ząbkowicki', 'Kamienna Nowa', 'Kamień Pomorski', 'Katowice', 'Katowice', 'Katowice Ligota', 'Kąty Wrocławskie', 'Kędzierzyn Koźle', 'Kępno', 'Kielce', 'Kiełpino Kartuskie', 'Kliniska', 'Kluczbork', 'Kłodawa', 'Kłodzko Główne', 'Knyszyn', 'Kobiór', 'Kolumna', 'Koluszki', 'Koło', 'Kołobrzeg', 'Kołodziejewo', 'Koniecpol', 'Konin', 'Konopki', 'Korsze', 'Korzeńsko', 'Kostów', 'Kostrzyn nad Odrą', 'Kostrzyn Wielkopolski', 'Koszalin', 'Koszęcin', 'Kościan', 'Kotlin', 'Kotomierz', 'Kowalewo Pomorskie', 'Kowalów', 'Koźmin Wielkopolski', 'Kraków Główny', 'Kraków Płaszów', 'Kraków Swoszowice', 'Krasiejów', 'Krotoszyn', 'Kruszyna', 'Krynica-Zdrój', 'Krzepice', 'Krzeszowice', 'Krzywizna', 'Krzyż Wielkopolski', 'Książki', 'Księginice', 'Kudowa Zdrój', 'Kundzin', 'Kutno', 'Kuźnica Białostocka', 'Laskowice Pomorskie', 'Lednogóra', 'Legnica', 'Leńcze', 'Leszno', 'Leżajsk', 'Lębork', 'Lipka Krajeńska', 'Lipno Nowe', 'Lubań Śląski', 'Lublin Główny', 'Lubliniec', 'Luboń koło Poznania', 'Lutol Suchy', 'Luzino', 'Łańcut', 'Łazy', 'Łęczyca', 'Łobez', 'Łowczówek Pleśna', 'Łowicz Główny', 'Łódź Chojny', 'Łódź Kaliska', 'Łódź Widzew', 'Łódź Żabieniec', 'Łódź Radogoszcz Zachód', 'Łódź Fabryczna', 'Łódź Retkinia', 'Łódź Lublinek', 'Łódź Koziny', 'Łódź Niciarniana', 'Łódź Olechów Wiadukt', 'Łódź Olechów Zachód', 'Łódź Olechów Wschód', 'Łódź Pabianicka', 'Łódź Stoki', 'Łódź Warszawska', 'Łódź Dąbrowa', 'Łódź Andrzejów', 'Ługi Górzyckie', 'Łuków', 'Machnacz', 'Maksymilianowo', 'Malbork', 'Malczyce', 'Małkinia', 'Małowice Wołowskie', 'Miały', 'Miasteczko Krajeńskie', 'Michalin', 'Miechów', 'Mieszkowice', 'Mieszków', 'Międzyborów', 'Międzylesie', 'Międzyrzec Podlaski', 'Międzyzdroje', 'Milanówek', 'Mińsk Mazowiecki', 'Mława', 'Modlin', 'Mogilno', 'Mokra', 'Mońki', 'Morąg', 'Morzeszczyn', 'Mosina', 'Mrozy', 'Myszków', 'Nakło nad Notecią', 'Nałęczów', 'Nasielsk', 'Nekla', 'Nidzica', 'Nieszawa Waganiec', 'Nowa Ruda', 'Nowa Sól', 'Nowa Wieś Mochy', 'Nowa Wieś Wielka', 'Nowe Drezdenko', 'Nowiny Wielkie', 'Nowogard', 'Nowy Sącz', 'Nowy Tomyśl', 'Oborniki Śląskie', 'Oborniki Wielkopolskie', 'Oborniki Wielkopolskie Miasto', 'Oborzyska Stare', 'Okonek', 'Olesno Śląskie', 'Oleśnica', 'Olsztyn Główny', 'Olsztyn Zachodni', 'Oława', 'Opalenica', 'Opoczno', 'Opole Główne', 'Opole Groszowice', 'Osie', 'Osielec', 'Osowiec', 'Ostrowie Biebrzańskie', 'Ostrów Wielkopolski', 'Ostrzeszów', 'Oświęcim', 'Otwock', 'Ozimek', 'Ożarów Mazowiecki', 'Pabianice', 'Palędzie', 'Pamiątkowo', 'Panki', 'Parlin', 'Pasłęk', 'Pępowo', 'Piaseczno', 'Piastów', 'Pierzchno', 'Pierzyska', 'Pilawa', 'Piła Główna', 'Piotrków Trybunalski', 'Pleszew', 'Płochocin', 'Płociczno koło Suwałk', 'Pobiedziska', 'Pobiedziska Letnisko', 'Podborsko', 'Podlasek', 'Polanica Zdrój', 'Pomniechówek', 'Poraj', 'Poronin', 'Potęgowo', 'Poznań Dębiec', 'Poznań Garbary', 'Poznań Główny', 'Poznań Główny (Nowy)', 'Poznań Główny (Stary)', 'Poznań Starołęka', 'Poznań Wola', 'Prabuty', 'Prudnik', 'Pruszcz Gdański', 'Pruszków', 'Przemyśl Główny', 'Przetycz', 'Przeworsk', 'Przyłubie', 'Przywory Opolskie', 'Pszczółki', 'Pszczyna', 'Puck', 'Puławy Miasto', 'Puszczykówko', 'Raba Wyżna', 'Rabka Zdrój', 'Racewo', 'Racibory', 'Racibórz', 'Racławice Śląskie', 'Radom', 'Radomsko', 'Radymno', 'Radziwiłłów Mazowiecki', 'Rawicz', 'Rogoźno Wielkopolskie', 'Rogów', 'Rokietnica', 'Roztoki Bystrzyckie', 'Ruda Śląska', 'Ruda Wielka', 'Rumia', 'Runowo Pomorskie', 'Ruszów', 'Rybnik', 'Rybnik Niedobczyce', 'Rybnik Paruszowiec', 'Rytel', 'Rzepin', 'Rzeszów Główny', 'Sątopy Samulewo', 'Serock', 'Sędzisław', 'Sędziszów', 'Sędziszów Małopolski', 'Sidra', 'Siechnice', 'Siedlce', 'Siemiatycze', 'Sieradz', 'Sierakowice', 'Sieraków Śląski', 'Silno', 'Skarżysko Kamienna', 'Skierniewice', 'Skokowa', 'Skorzewo', 'Sławięcice', 'Sławno', 'Słonice', 'Słupca', 'Słupsk', 'Smardzów Wrocławski', 'Smętowo', 'Smolec', 'Sochaczew', 'Sopot', 'Sosnowiec Główny', 'Sośnie Ostrowskie', 'Stalowa Wola', 'Staniszcze Małe', 'Stara Łubianka', 'Starczów', 'Stare Bojanowo', 'Stare Kurowo', 'Stare Pole', 'Stargard', 'Starogard Gdański', 'Sterkowiec', 'Stęszew', 'Stronie', 'Stryków', 'Stryszów', 'Strzałkowo', 'Strzelce Krajeńskie Wsch.', 'Strzelce Opolskie', 'Strzelin', 'Sucha Beskidzka', 'Suchedniów', 'Sulechów', 'Sulejówek Miłosna', 'Sułkowice', 'Sumina Wieś', 'Susz', 'Suwałki', 'Swarzędz', 'Szamotuły', 'Szczecin Dąbie', 'Szczecin Główny', 'Szczecinek', 'Szczepki', 'Szczytna', 'Szczytno', 'Szepietowo', 'Szklarska Poręba Górna', 'Szlachta', 'Sztum', 'Szydłów', 'Szymiszów', 'Ścinawa', 'Ścinawka Średnia', 'Ślesin', 'Środa Wielkopolska', 'Świdwin', 'Świebodzice', 'Świebodzin', 'Świekatowo', 'Święta Katarzyna', 'Świnoujście', 'Taczanów', 'Tarnowskie Góry', 'Tarnów', 'Tczew', 'Terespol', 'Tłuszcz', 'Tomaszów Mazowiecki', 'Toruń Miasto', 'Toruń Wschodni', 'Trakiszki', 'Trzcianka', 'Trzebiatów', 'Trzebinia', 'Trzemeszno', 'Turzno', 'Twarda Góra', 'Tychowo', 'Tychy', 'Wałbrzych Główny', 'Wałbrzych Miasto', 'Warka', 'Warszawa Centralna', 'Warszawa Choszczówka', 'Warszawa Dawidy', 'Warszawa Falenica', 'Warszawa Gdańska', 'Warszawa Główna', 'Warszawa Gocławek', 'Warszawa Gołąbki', 'Warszawa Jeziorki', 'Warszawa Koło Nowy', 'Warszawa Lotnisko Chopina', 'Warszawa Miedzeszyn', 'Warszawa Międzylesie', 'Warszawa Młynów', 'Warszawa Mokry Ług', 'Warszawa Ochota', 'Warszawa Okęcie', 'Warszawa Olszynka Grochowska', 'Warszawa Płudy', 'Warszawa Powązki', 'Warszawa Powiśle', 'Warszawa Praga', 'Warszawa Radość', 'Warszawa Raków Wkd', 'Warszawa Rakowiec', 'Warszawa Reduta Ordona', 'Warszawa Rembertów', 'Warszawa Salomea Wkd', 'Warszawa Służewiec', 'Warszawa Śródmieście', 'Warszawa Śródmieście WKD', 'Warszawa Stadion', 'Warszawa Targówek', 'Warszawa Toruńska', 'Warszawa Ursus', 'Warszawa Ursus Niedźwiadek', 'Warszawa Ursus Północny', 'Warszawa Wawer', 'Warszawa Wesoła', 'Warszawa Wileńska', 'Warszawa Włochy', 'Warszawa Wola', 'Warszawa Wola Grzybowska', 'Warszawa Wschodnia', 'Warszawa Zachodnia', 'Warszawa Zachodnia P9', 'Warszawa Zacisze Wilno', 'Warszawa Żerań', 'Warszawa Aleje Jerozolimskie', 'Warszawa Anin', 'Warszawa Zoo', 'Warszawa Żwirki i Wigury', 'Wasilków', 'Wąbrzeźno', 'Wejherowo', 'Wejherowo Nanice', 'Wieliczka Park', 'Wierzchowo Człuchowskie', 'Wierzchucin', 'Wilkoszewice', 'Witaszyce', 'Witnica', 'Władysławowo', 'Włocławek', 'Włocławek Zazamcze', 'Włoszakowice', 'Włoszczowa', 'Wolin', 'Wołczyn', 'Wrocław Brochów', 'Wrocław Główny', 'Wrocław Kuźniki', 'Wrocław Leśnica', 'Wrocław Mikołajów Wp2', 'Wrocław Osobowice', 'Wrocław Pracze', 'Wrocław Psie Pole', 'Wrocław Zachodni', 'Wronki', 'Września', 'Wschowa', 'Wydminy', 'Wyrzysk-Osiek', 'Zabrze', 'Zalesie Górne', 'Zawadzkie', 'Zawiercie', 'Ząbki', 'Ząbkowice Śląskie', 'Zbąszynek', 'Zbąszynek', 'Zbąszyń', 'Zblewo', 'Zdrody Nowe', 'Zdzieszowice', 'Zebrzydowice', 'Zgierz', 'Zgierz Północ', 'Zgierz Kontrewers', 'Zgierz Jaracza', 'Zgorzelec', 'Zielona Góra Główna', 'Zielonczyn', 'Ziębice', 'Złocieniec', 'Złotniki Kujawskie', 'Złotów', 'Żagań', 'Żarów', 'Żary', 'Żmigród', 'Żukowo Wschodnie', 'Życzyn', 'Żyrardów', 'Żytkowice', 'Żywiec'])

time.sleep(5)

FirstStationPrompt = prompt('Stacja Początkowa 🢒 ', completer=stations_list)
LastStationPrompt = prompt('Stacja Końcowa 🢒 ', completer=stations_list)

print("\n")
print("Wyszukiwanie Połączenia... ↻")
print("\n")

stacja_poczatkowa_ext = ("A=1@O="+FirstStationPrompt)
stacja_docelowa_ext = ("A=1@O="+LastStationPrompt)

dane = {'fromStation': {FirstStationPrompt}, 'poczatkowa': {stacja_poczatkowa_ext}, 'toStation': {LastStationPrompt}, 'docelowa': {stacja_docelowa_ext}, 'data': {czas_payload}, 'date': {aktualna_data}, 'time': {current_time}, 'przyjazd': 'false', 'minChangeTime': '10', 'bilkomAvailOnly': 'on'}
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.5', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

index_search = "https://bilkom.pl/podroz?basketKey=&carrierKeys=P2,P1,P5,P9,P7,O1,PZ"
RequestedBilkomLink = requests.get(index_search, params=dane, headers=headers)
SeleniumDriver.get(RequestedBilkomLink.url)
SeleniumDriver.execute_script("changePage(nextPageLink, 1)")
time.sleep(8)
BilkomSourceCode = SeleniumDriver.page_source
SeleniumDriver.quit()

BilkomStrona = BeautifulSoup(BilkomSourceCode, "html.parser")

WylistowaneTripy = BilkomStrona.find_all("li", {"class": "el"})

print("Znalezione Połączenia ↓")
time.sleep(1)
print("\n")

for item in WylistowaneTripy:
	TrasaPociagu_FS = item.find("li", {"class": "first-r"})
	TrasaPociagu_PierwszaStacja = TrasaPociagu_FS.find("span", {"class": "main-station"}).text
	TrasaPociagu_LS = item.find("li", {"class": "last-r"})
	TrasaPociagu_OstatniaStacja = TrasaPociagu_LS.find("span", {"class": "main-station"}).text
	Peron_PierwszaStacja = TrasaPociagu_FS.find("span", {"class": "main-station"})
	Peron_OstatniaStacja = TrasaPociagu_LS.find("span", {"class": "main-station"})
	NumerPociagu = item.find("div", {"class": "carriers-wrapper"}).text
	CzasOdjazdu = item.find("li", {"class": "first-r"}).find("span", {"class": "arrival-time"}).text
	CzasPrzyjazdu = item.find("li", {"class": "last-r"}).find("span", {"class": "arrival-time"}).text
	OpozniniaPociagu = "0"
	FindCenaPrzejazdu = item.find("span", {"class": "price-wrapper"})
	PrzesiadkiPociagu = item.find("div", {"class": "changes"}).text
	CzasPodrozy = item.find("span", {"class": "duration"}).text
	ListowaniePrzewoznikow = item.find_all("div", {"class": "carrier"})

	PStrip = PrzesiadkiPociagu.replace("Przesiadki:", "")
	PStrip2 = PStrip.replace(" ", "")
	PStrip3 = PStrip2.strip()

	if Peron_PierwszaStacja.has_attr('data-peron'):
		PeronPierwszy = Peron_PierwszaStacja['data-peron']
	else:
		PeronPierwszy = "N/A"

	if Peron_OstatniaStacja.has_attr('data-peron'):
		PeronOstatni = Peron_OstatniaStacja['data-peron']
	else:
		PeronOstatni = "N/A"

	print(f"Trasa Pociągu: {TrasaPociagu_PierwszaStacja.strip()} [{PeronPierwszy}] → {TrasaPociagu_OstatniaStacja.strip()} [{PeronOstatni}]\n")

	ListaNumPoc = ""
	for przewoznik in ListowaniePrzewoznikow:
		NumPoc = przewoznik.find("div", {"class": "hidden"}).text
		ListaNumPoc+=(str(NumPoc)+"\n")
		
	print(f"⮮ Przewoznik/cy\n")
	print(f"{ListaNumPoc}") 
	print(f"Godzina Odjazdu 🢒 {CzasOdjazdu}")
	print(f"Godzina Przyjazdu 🢒 {CzasPrzyjazdu}")
	print(f"Ilość Przesiadek 🢒 {PStrip3}")
	print(f"Czas Podróży 🢒 {CzasPodrozy}\n")

	if FindCenaPrzejazdu:
		CenaPrzejazdu = item.find("span", {"class": "price-wrapper"}).find("span", {"class": "price"}).text
		CenaPrzejazduOut = print(f"Cena Przejazdu 🢒\033[1;32;40m {CenaPrzejazdu} \033[0;37;40mZŁ\n")
	else:
		CenaPrzejazduOut = print(f"Cena Przejazdu 🢒\033[1;31;40m Niedostępna\033[0;37;40m\n")

	print("————————————————————————————————————————\n")

print(f"Link do podanych połączeń ⮯")
print(RequestedBilkomLink.url)