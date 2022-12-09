import psycopg2
import os
import logging
logging.basicConfig(level=logging.INFO)

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()


def delete_tasks() -> None:
    with psycopg2.connect(os.environ['DATABASE_URL']) as conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM todos")
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


@sched.scheduled_job('interval', minutes=2)
def main():
    delete_tasks()


if __name__ == '__main__':
    delete_tasks()
    try:
        logging.info(f"\n DAEMON BOT START \n")
        sched.start()
    except Exception as e:
        logging.error(f"\n DAEMON BOT error: \n{e}")
