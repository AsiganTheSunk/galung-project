import os
import re
import sys
import math
import time
import glob
import shlex
import logging
import subprocess

from lxml import etree
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler
from main.ffmpeg.configuration import read_config


# def execute_run(args):
#     config = read_config()
#     log_file = get_log_file()
#
#     log = logging.getLogger('')
#     log.setLevel(logging.DEBUG)
#     format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#
#     ch = logging.StreamHandler(sys.stdout)
#     ch.setFormatter(format)
#     log.addHandler(ch)
#
#     fh = RotatingFileHandler(log_file, maxBytes=(1048576*100), backupCount=7)
#     fh.setFormatter(format)
#     log.addHandler(fh)
#
#     args = {key: value for key, value in args.items() if value}
#     for key, value in args.items():
#         if key == 'directory':
#             directory = value
#         # Encoding
#         if key == 'crf':
#             config['encoding']['crf'] = str(value)
#         elif key == 'preset':
#             config['encoding']['preset'] = value
#         elif key == 'audio':
#             config['encoding']['audio'] = value
#         elif key == 'audio':
#             config['encoding']['kbitrate-audio'] = value
#         elif key == 'threads':
#             config['encoding']['threads'] = str(value)
#
#     if not directory or not os.path.isdir(directory):
#         logging.warning('A valid directory needs to be specified')
#         logging.warning(directory)
#         sys.exit(1)
#     else:
#         # Get absolute path of directory
#         directory = os.path.abspath(directory)
#
#     files = find_files(directory)
#
#     processed_files = 0
#     for path in files:
#         # Get absolute path
#         path = os.path.abspath(path)
#         # Create media info and get `Writing library` value.
#         mediainfo = get_media_encoding(path)
#         if 'x265' in mediainfo:
#             continue
#
#         # Get directory the movie is in and the name for new encoded video file.
#         directory_path = os.path.dirname(path)
#         # Change filename to contain 'x265'.
#         # Replace it if there is a 'x264' in the filename.
#         dest_file = os.path.basename(path)
#         dest_folder = os.path.dirname(path)
#         if 'x264' in dest_file:
#             dest_file = dest_file.replace('x264', 'x265')
#             dest_path = os.path.join(dest_folder, dest_file)
#             dest_path = os.path.splitext(dest_path)[0] + '.mkv'
#         # Add a `-x265.mkv` if there is nothing to replace
#         else:
#             dest_path = os.path.splitext(path)[0] + '-x265.mkv'
#
#         # Compile ffmpeg command
#         ffmpeg_command = create_ffmpeg_command(config, path, dest_path)
#
#         # Check if the current command already in the queue.
#         index, status = get_current_index(ffmpeg_command)
#
#         # Send the command to pueue for scheduling, if it isn't in the queue yet
#         if index is None and status is None:
#             # In case a previous run failed and pueue has been resetted,
#             # we need to check, if the encoded file is still there.
#             if os.path.exists(dest_path):
#                 os.remove(dest_path)
#             args = {
#                 'command': ffmpeg_command,
#                 'path': directory_path
#             }
#             logging.info("Add task pueue:\n {}".format(ffmpeg_command))
#             execute_add(args)
#         else:
#             logging.info("Task already exists in pueue: \n{}".format(ffmpeg_command))
#
#         waiting = True
#         while waiting:
#             # Get index of current command and the current status
#             index, status = get_current_index(ffmpeg_command)
#             # If the command has been removed or errored,
#             # remove the already created destination file
#             if (index is None and status is None) or status == 'errored':
#                 if os.path.exists(dest_path):
#                     os.remove(dest_path)
#                 waiting = False
#             # If the command has finished, break the loop for further processing
#             elif status == 'done':
#                 waiting = False
#
#             time.sleep(60)
#
#         if os.path.exists(dest_path):
#             logging.info("Pueue task completed")
#             copy = True
#             # If the destination movie is shorter than a maximum of 20 seconds
#             # as the original or has no duration property in mediafmkvile, we drop this.
#             origin_duration = get_media_duration(path)
#             dest_duration = get_media_duration(dest_path)
#             if dest_duration is not None:
#                 diff = origin_duration - dest_duration
#                 THRESHOLD = 20
#                 if math.fabs(diff.total_seconds()) > THRESHOLD:
#                     logging.warning('Encoded movie is more than {} shorter/longer than original.'.format(THRESHOLD))
#                     copy = False
#
#             # Check if the filesize of the x.265 encoded object is bigger
#             # than the original.
#             if copy:
#                 origin_filesize = os.path.getsize(path)
#                 dest_filesize = os.path.getsize(dest_path)
#                 if origin_filesize < dest_filesize:
#                     logging.warning('Encoded movie is bigger than the original movie')
#                     copy = False
#                 else:
#                     difference = origin_filesize - dest_filesize
#                     mebibyte = int(difference/1024/1024)
#                     logging.info('The new movie is {} MIB smaller than the old one'.format(mebibyte))
#
#             # Only copy if checks above passed
#             if copy:
#                 os.remove(path)
#                 processed_files += 1
#                 logging.info("New encoded file is now in place")
#             else:
#                 logging.warning("Didn't copy new file, see message above")
#         else:
#             logging.error("Pueue task failed in some kind of way.")
#
#     if processed_files == 0:
#         logging.info('No files for encoding found')
#     else:
#         logging.info('{} movies successfully encoded. Exiting'.format(processed_files))
#
#
# def find_files(path):
#     """Get all known video files by recursive extension search."""
#     extensions = ['mkv', 'mp4', 'avi']
#     files = []
#     for extension in extensions:
#         found = glob.glob(
#             os.path.join(path, '**/*.{}'.format(extension)),
#             recursive=True)
#         files = files + found
#     return files
#
#
# def create_ffmpeg_command(config, path, dest_path):
#     """Compile an ffmpeg command by known parameters."""
#     if config['encoding']['kbitrate-audio'] != 'None':
#         audio_bitrate = '-b:a {}'.format('audio_bitrate')
#     else:
#         audio_bitrate = ''
#     ffmpeg_command = 'ffmpeg -i {path} -c:v libx265 -preset {preset} ' \
#         '-x265-params crf={crf}:pools=none -threads {threads} -c:a {audio} {bitrate} {dest}'.format(
#             path=shlex.quote(path),
#             dest=shlex.quote(dest_path),
#             preset=config['encoding']['preset'],
#             crf=config['encoding']['crf'],
#             threads=config['encoding']['threads'],
#             audio=config['encoding']['audio'],
#             bitrate=audio_bitrate,
#         )
#     return ffmpeg_command
