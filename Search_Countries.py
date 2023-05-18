from tkinter import *


#===================== Frontend_1 =====================

Root = Tk()
Root.title("Search Countries")
Root.geometry("500x550")

#===================== Backend_1 =====================
#================= Data Base1 =================
Names_Of_Countries = {"A":"""Afghanistan;
Albania;
Algeria;
Andorra;
Angola;
Antigua and Barbuda;
Argentina;
Armenia;
Australia;
Austria;
Austrian Empire;
Azerbaijan""", "B":"""
Baden*;
Bahamas, The;
Bahrain;
Bangladesh;
Barbados;
Bavaria*;
Belarus;
Belgium;
Belize;
Benin (Dahomey);
Bolivia;
Bosnia and Herzegovina;
Botswana;
Brazil;
Brunei;
Brunswick and Lüneburg;
Bulgaria;
Burkina Faso (Upper Volta);
Burma;
Burundi""", "C":"""
Cabo Verde;
Cambodia;
Cameroon;
Canada;
Cayman Islands, The;
Central African Republic;
Central American Federation*;
Chad;
Chile;
China;
Colombia;
Comoros;
Congo Free State, The;
Costa Rica;
Cote d’Ivoire (Ivory Coast);
Croatia;
Cuba;
Cyprus;
Czechia;
Czechoslovakia""", "D":"""
Democratic Republic of the Congo;
Denmark;
Djibouti;
Dominica;
Dominican Republic;
Duchy of Parma, The*""", "E":"""
East Germany (German Democratic Republic)*;
Ecuador;
Egypt;
El Salvador;
Equatorial Guinea;
Eritrea;
Estonia;
Eswatini;
Ethiopia""", "F":"""
Federal Government of Germany (1848-49)*;
Fiji;
Finland;
France""", "G":"""
Gabon;
Gambia, The;
Georgia;
Germany;
Ghana;
Grand Duchy of Tuscany, The*;
Greece;
Grenada;
Guatemala;
Guinea;
Guinea-Bissau;
Guyana""", "H":"""
Haiti;
Hanover*;
Hanseatic Republics*;
Hawaii*;
Hesse*;
Holy See;
Honduras;
Hungary""", "I":"""
Iceland;
India;
Indonesia;
Iran;
Iraq;
Ireland;
Israel;
Italy""", "J":"""
Jamaica;
Japan;
Jordan""", "K":"""
Kazakhstan;
Kenya;
Kingdom of Serbia/Yugoslavia*;
Kiribati;
Korea;
Kosovo;
Kuwait;
Kyrgyzstan""", "L":"""
Laos;
Latvia;
Lebanon;
Lesotho;
Lew Chew (Loochoo)*;
Liberia;
Libya;
Liechtenstein;
Lithuania;
Luxembourg""", "M":"""
Madagascar;
Malawi;
Malaysia;
Maldives;
Mali;
Malta;
Marshall Islands;
Mauritania;
Mauritius;
Mecklenburg-Schwerin*;
Mecklenburg-Strelitz*;
Mexico;
Micronesia;
Moldova;
Monaco;
Mongolia;
Montenegro;
Morocco;
Mozambique""", "N":"""
Namibia;
Nassau*;
Nauru;
Nepal;
Netherlands, The;
New Zealand;
Nicaragua
Niger;
Nigeria;
North German Confederation*;
North German Union*;
North Macedonia;
Norway""", "O":"""
Oldenburg*;
Oman;
Orange Free State*""", "P":"""
Pakistan;
Palau;
Panama;
Papal States*;
Papua New Guinea;
Paraguay;
Peru;
Philippines;
Piedmont-Sardinia*;
Poland;
Portugal""", "Q":"""
Qatar""", "R":"""
Republic of Genoa*;
Republic of Korea (South Korea);
Republic of the Congo;
Romania;
Russia;
Rwanda""", "S":"""
Saint Kitts and Nevis;
Saint Lucia;
Saint Vincent and the Grenadines;
Samoa;
San Marino;
Sao Tome and Principe;
Saudi Arabia;
Schaumburg-Lippe*;
Senegal;
Serbia;
Seychelles;
Sierra Leone;
Singapore;
Slovakia;
Slovenia;
Solomon Islands, The;
Somalia;
South Africa;
South Sudan;
Spain;
Sri Lanka;
Sudan;
Suriname;
Sweden;
Switzerland;
Syria""", "T":"""
Tajikistan;
Tanzania;
Texas*;
Thailand;
Timor-Leste;
Togo;
Tonga;
Trinidad and Tobago;
Tunisia;
Turkey;
Turkmenistan;
Tuvalu;
Two Sicilies*""", "U":"""
Uganda;
Ukraine;
Union of Soviet Socialist Republics*;
United Arab Emirates, The;
United Kingdom, The;
Uruguay;
Uzbekistan""", "V":"""
Vanuatu;
Venezuela;
Vietnam""", "W":"""
Württemberg*""","Y":"""
Yemen""", "Z":"""
Zambia;
Zimbabwe"""}

#==================== Data Base2 =====================

Countries_Prefix = {"A":"""Afghanistan 93;
Albania 355;
Algeria 213;
American Samoa 1 684;
Andorra 376;
Angola 244;
Anguilla 1 264;
Antarctica (Australian bases) 6721;
Antigua and Barbuda 1 268;
Argentina 54;
Armenia 374;
Aruba 297;
Ascension 247;
Australia 61;
Austria 43;
Azerbaijan 994""","B":"""
Bahamas 1 242;
Bahrain 973;
Bangladesh 880;
Barbados 1 246;
Belarus 375;
Belgium 32;
Belize 501;
Benin 229;
Bermuda 1 441;
Bhutan 975;
Bolivia 591;
Bonaire, Sint Eustatius and Saba 599;
Bosnia and Herzegovina 387;
Botswana 267;
Brazil 55;
British Indian Ocean Territory 246;
British Virgin Islands 1 284;
Brunei 673;
Bulgaria 359;
Burkina Faso 226;
Burundi 257""","C":"""
Cabo Verde 238;
Cambodia 855;
Cameroon 237;
Canada 1;
Cayman Islands 1 345;
Central African Republic 236;
Chad 235;
Chile 56;
China 86;
Colombia 57;
Comoros 269;
Congo, Democratic Republic of the 243;
Congo, Republic of the 242;
Cook Islands 682;
Costa Rica 506;
Cote d'Ivoire 225;
Croatia 385;
Cuba 53;
Curaçao 599;
Cyprus 357;
Czech Republic 420""","D":"""
Denmark 45;
Djibouti 253;
Dominica 1 767;
Dominican Republic 1 809, 1 829, and 1 849""","E":"""
Ecuador 593;
Egypt 20;
El Salvador 503;
Equatorial Guinea 240;
Eritrea 291;
Estonia 372;
Eswatini 268;
Ethiopia 251""","F":"""
Falkland Islands 500;
Faroe Islands 298;
Fiji 679;
Finland 358;
France 33;
French Guiana 594;
French Polynesia 689""","G":"""
Gabon 241;
Gambia 220;
Gaza Strip 970;
Georgia (and parts of breakaway regions; Abkhazia as well as South Ossetia) 995;
Germany 49;
Ghana 233;
Gibraltar 350;
Greece 30;
Greenland 299;
Grenada 1 473;
Guadeloupe 590;
Guam 1 671;
Guatemala 502;
Guinea 224;
Guinea-Bissau 245;
Guyana 592""","H":"""
Haiti 509;
Honduras 504;
Hong Kong 852;
Hungary 36""","I":"""
Iceland 354;
India 91;
Indonesia 62;
Iraq 964;
Iran 98;
Ireland (Eire) 353;
Israel 972;
Italy 39""","J":"""
Jamaica 1 876, 1 658;
Japan 81;
Jordan 962""","K":"""
Kazakhstan 7;
Kenya 254;
Kiribati 686;
Kosovo 383;
Kuwait 965;
Kyrgyzstan 996""","L":"""
Laos 856;
Latvia 371;
Lebanon 961;
Lesotho 266;
Liberia 231;
Libya 218;
Liechtenstein 423;
Lithuania 370;
Luxembourg 352""","M":"""
Macau 853;
Madagascar 261;
Malawi 265;
Malaysia 60;
Maldives 960;
Mali 223;
Malta 356;
Marshall Islands 692;
Martinique 596;
Mauritania 222;
Mauritius 230;
Mayotte 262;
Mexico 52;
Micronesia Federated States of 691;
Moldova (plus breakaway Pridnestrovie) 373;
Monaco 377;
Mongolia 976;
Montenegro 382;
Montserrat 1 664;
Morocco 212;
Mozambique 258;
Myanmar 95""","N":"""
Namibia 264;
Nauru 674;
Netherlands 31;
Nepal 977;
New Caledonia 687;
New Zealand 64;
Nicaragua 505;
Niger 227;
Nigeria 234;
Niue 683;
Norfolk Island 6723;
North Korea 850;
North Macedonia 389;
Northern Ireland 44 28;
Northern Mariana Islands 1 670;
Norway 47""","O":"""
Oman 968""","P":"""
Pakistan 92;
Palau 680;
Palestine 970;
Panama 507;
Papua New Guinea 675;
Paraguay 595;
Peru 51;
Philippines 63;
Poland 48;
Portugal 351;
Puerto Rico 1 787 and 1 939""","Q":"""
Qatar 974""","R":"""
Reunion 262;
Romania 40;
Russia 7;
Rwanda 250""","S":"""
Saint-Barthélemy 590;
Saint Helena and Tristan da Cunha 290;
Saint Kitts and Nevis 1 869;
Saint Lucia 1 758;
Saint Martin (French side) 590;
Saint Pierre and Miquelon 508;
Saint Vincent and the Grenadines 1 784;
Samoa 685;
Sao Tome and Principe 239;
Saudi Arabia 966;
Senegal 221;
Serbia 381;
Seychelles 248;
Sierra Leone 232;
Sint Maarten (Dutch side) 1 721;
Singapore 65;
Slovakia 421;
Slovenia 386;
Solomon Islands 677;
Somalia 252;
South Africa 27;
South Korea 82;
South Sudan 211;
Spain 34;
Sri Lanka 94;
Sudan 249;
Suriname 597;
Sweden 46;
Switzerland 41;
Syria 963""","T":"""
Taiwan 886;
Tajikistan 992;
Tanzania 255;
Thailand 66;
Timor-Leste 670;
Togo 228;
Tokelau 690;
Tonga 676;
Trinidad and Tobago 1 868;
Tunisia 216;
Turkey 90;
Turkmenistan 993;
Turks and Caicos Islands 1 649;
Tuvalu 688""","U":"""
Uganda 256;
Ukraine 380;
United Arab Emirates 971;
United Kingdom 44;
United States of America 1;
Uruguay 598;
Uzbekistan 998""","V":"""
Vanuatu 678;
Venezuela 58;
Vietnam 84;
U.S. Virgin Islands 1 340""","W":"""
Wallis and Futuna 681;
West Bank 970""","Y":"""
Yemen 967""","Z":"""
Zambia 260;
Zimbabwe 263"""}

#===================== Frontend_2 =====================
#================= Labels =================

Txt0 = StringVar()
Txt0.set("Names of countries:")
Label0 = Label(Root, textvariable=Txt0)
Label0.place(x=10, y=10)

Txt1 = StringVar()
Txt1.set("Enter the first character of the country name:")
Label1 = Label(Root, textvariable=Txt1)
Label1.place(x=10, y=30)

Txt2 = StringVar()
Txt2.set("List of mobile telephone prefixes by country:")
Label2 = Label(Root, textvariable=Txt2)
Label2.place(x=10, y=290)

Txt3 = StringVar()
Txt3.set("Enter the first character of the country name:")
Label3 = Label(Root, textvariable=Txt3)
Label3.place(x=10, y=310)

#================= Entries =================
Txt_E1 = StringVar()
Entry1 = Entry(Root, textvariable=Txt_E1)
Entry1.place(x=250, y=30)

Txt_E2 = StringVar()
Entry2 = Entry(Root, textvariable=Txt_E2)
Entry2.place(x=250, y=310)

#================= List Boxes & Scrollbars =================
list_Box = Listbox(Root, width=50, height=10)
list_Box.place(x=90, y=70)

SB1 = Scrollbar(Root)
SB1.place(x=400, y=120)

list_Box.configure(yscrollcommand=SB1.set)
SB1.configure(command=list_Box.yview)

list_Box2 = Listbox(Root, width=50, height=10)
list_Box2.place(x=90, y=340)

SB2 = Scrollbar(Root)
SB2.place(x=400, y=390)

list_Box2.configure(yscrollcommand=SB2.set)
SB2.configure(command=list_Box2.yview)

#===================== Backend_2 =====================
#================= Functions =================

def Show_All():
    list_Box.delete(0, END)
    for key in Names_Of_Countries:
        list_b1 = Names_Of_Countries[key].split(";")
        for NAME in list_b1:
            list_Box.insert(END, NAME)
Show_All()

def Show_All2():
    list_Box2.delete(0, END)
    for key in Countries_Prefix:
        list_b2 = Countries_Prefix[key].split(";")
        for NAME in list_b2:
            list_Box2.insert(END, NAME)
Show_All2()

def View_Names(key):
    try:
        list_Box.delete(0,END)
        list_b1 = Names_Of_Countries[key.upper()].split(";")
        for NAME in list_b1:
            list_Box.insert(END, NAME)
    except KeyError:
        list_Box.delete(0, END)
        if key == "X" or key == "x":
            Error = "We do not have a country with the word 'X'"
        else:
            Error = "Key Error"
        list_Box.insert(END, Error)

def View_Prefix(key):
    try:
        list_Box2.delete(0,END)
        list_b2 = Countries_Prefix[key.upper()].split(";")
        for NAME in list_b2:
            list_Box2.insert(END, NAME)
    except KeyError:
        list_Box2.delete(0, END)
        if key == "X" or key == "x":
            Error = "We do not have a country with the word 'X'"
        else:
            Error = "Key Error"
        list_Box2.insert(END, Error)

#===================== Frontend_3 =====================
#=================# Buttons =================
Search_btn = Button(Root, text="Search", width=10, command=lambda: View_Names(Entry1.get()))
Search_btn.place(x=385,y=27)

Show_All_btn = Button(Root, text="Show all", width=10, command=Show_All)
Show_All_btn.place(x=200, y=240)

Search_btn2 = Button(Root, text="Search", width=10, command=lambda: View_Prefix(Entry2.get()))
Search_btn2.place(x=385,y=307)

Show_All_btn2 = Button(Root, text="Show all", width=10, command=Show_All2)
Show_All_btn2.place(x=200, y=510)


Root.mainloop()
