import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

path_json = "../creds/energoprof-387808-a62ef73bdda0.json"

creds_auth = ServiceAccountCredentials \
    .from_json_keyfile_name(path_json, ['https://www.googleapis.com/auth/spreadsheets']) \
    .authorize(httplib2.Http())

service = build('sheets', 'v4', http=creds_auth)

sss = service.spreadsheets()

wilo_id = "1k2HNdWadastO5xhkW6BA3WTkpxDYHPxdhromodR9RL4"
sheet_id = "1PEN4bHKM-qNdMhJTE8vxwYZT3BRPu1M8ia_kLWTjZTM"

# r = sss.values().get(spreadsheetId=sheet_id, range="Лист1!A1:B2").execute()
r_w = sss.values().get(spreadsheetId=wilo_id, range="Wilo!A4:B41").execute()

# resp = sss.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1", "Лист2"]).execute()
# resp_w = sss.values().batchGet(spreadsheetId=wilo_id, ranges=["Wilo!A4", "Wilo!A5"]).execute()
# for key, value in resp_w.items():
#     print(f'{value},')
#
# rr = resp_w.get('valueRanges', [])

#
# netangels

gg = r_w.get('values', [])
# print(gg)
num = [0, 0]
name = input()

for index1 in range(len(gg)):
    for index2 in range(0, 2, 1):
        if gg[index1][index2] == name:
            print("Yes")
            num = [index1, index2]

print(num)

val = num[0] + 4
next_r = sss.values().get(spreadsheetId=wilo_id, range=f"Wilo!A{val}:K{val}").execute()

ll = next_r.get('values', [])
print(ll)
# print(num)
