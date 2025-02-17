from modules import classifications as cl
import time

start_time = time.time()

sheet_curr = '1wxR3iYna86qrdViwHjUPzHuw6bCNeMLb72M25hpUHYk'
sheet_archive = '1PxNYGMXaVrRqI0uyMQF46K7nDEG16WnDoKrFyI_qrvE'
gid_matches = '2141931777'
gid_deck = '590005429'

df_valid_decks, df_valid_event_types = cl.parse_class_sheet(sheet_curr, gid_deck)
cl.class_insert(df_valid_decks, df_valid_event_types)

print(time.time() - start_time)