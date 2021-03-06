# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import argparse
from textwrap import dedent

from markdown import CsvToMarkdownConverter
from opml import OpmlToCsvConverter, CsvToOpmlConverter
from taskpaper import CsvToTaskPaperConverter

FORMAT_MD = 'md'
FORMAT_OPML = 'opml'
FORMAT_CSV = 'todoist'
FORMAT_TASKPAPER = 'taskpaper'


def convert(args):
    """
    Convert file to specified format.
    Rows: TYPE (task, note),CONTENT,PRIORITY(1-4),INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG
    """

    if args.format.lower() == FORMAT_OPML:
        klass = CsvToOpmlConverter
    elif args.format.lower() == FORMAT_CSV:
        klass = OpmlToCsvConverter
    elif args.format.lower() == FORMAT_TASKPAPER:
        klass = CsvToTaskPaperConverter
    else: 
        klass = CsvToMarkdownConverter

    conv = klass(args)    
    if args.output:
        conv.target_name = args.output
    conv.convert()

def main():
    parser = argparse.ArgumentParser(
        description=dedent("""Convert Todoist template files (and Todoist backups) to other formats.
            To convert an entire backup use 
            ls -bp | xargs -I xx tdconv -df taskpaper "xx"
            """))

    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='increase level of verbosity (repeat up to 3 times)')
    parser.add_argument('--format', '-f', default='md',
                        help='format of target file: md, opml, todoist, taskpaper')
    parser.add_argument('--output', '-o', default=None,
                        help='name of target file, if this argument is not present, name of source file will be used')
    parser.add_argument('--download', '-d', action="store_true", default=False,
                        help='download attachments')
    parser.add_argument('file',
                        help='file to convert')
    
    args = parser.parse_args()
    convert(args)
