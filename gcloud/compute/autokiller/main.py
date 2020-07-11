import os
import re
import subprocess

from mcrcon import MCRcon

MC_HOST = 'localhost'
MC_PASS = '114514'
SHUTDOWN_FLAG = '/tmp/shutdown-flag'

def main():
    p = re.compile('\d+')
    with MCRcon(MC_HOST, MC_PASS) as mcr:
        res_list = mcr.command('/list')
        player_count = int(p.findall(res_list)[0])

    if player_count > 0:
        os.remove(SHUTDOWN_FLAG) if os.path.exists(SHUTDOWN_FLAG) else None
        return

    if os.path.exists(SHUTDOWN_FLAG):
        """Shutdown now!"""
        with MCRcon(MC_HOST, MC_PASS) as mcr:
            mcr.command('/stop')
        subprocess.run('gcloud functions call stop')
    else:
        """Shutdown at next"""
        with open(SHUTDOWN_FLAG, mode='w') as f:
            f.write('')

main()
