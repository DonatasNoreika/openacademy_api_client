import config
import xmlrpc.client
import functools

ROOT = f'http://{config.HOST}:{config.PORT}/xmlrpc/'

uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(config.DB, config.USER, config.PASS)

print(f"Logged in as {config.USER} (uid:{uid})")

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    config.DB, uid, config.PASS)

def print_all_session():
    sessions = call('openacademy.session', 'search_read', [], ['name', 'seats'])
    for session in sessions:
        print(f'{session["id"]}: {session["name"]}, seats: {session["seats"]}')

def add_course(name, description):
    course_id = call('openacademy.course', 'create', {
        'name': name,
        'description': description,
    })

# print_all_session()
# add_course("Kursas 22", "Dvidešimt antras kursas")