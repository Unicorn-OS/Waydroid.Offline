import os
import subprocess

def getPath():
    image = "lineage-18.1-20241012-GAPPS-waydroid_x86_64-system.zip"

    cache = f"/home/{os.environ.get('USER')}/Downloads/"
    path = "/var/lib/waydroid/cache_http/"
    hexdigest = "ed4f9371fa7b5da965a0dc972f70a2d43ffe9bc1a25f3c1c12a7390e2a9f7db1"

    global rsync_from, rsync_to
    rsync_from = f"{cache}{image}"
    rsync_to = f"{path}{image}_{hexdigest}"

def syncCache():
    getPath()
    subprocess.call(["rsync", "-av", "--progress", rsync_from, rsync_to])


syncCache()