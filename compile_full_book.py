#!/usr/bin/env python3

import re

TOC_CHAPTER_PATTERN = re.compile(r'- \[(?P<name>[^\]]+)\]\((?P<path>[^)]+)\)')
IMAGE_LINK_PATTERN = re.compile(r'!\[(?P<name>[^\]]+)\]\((?P<path>[^)]+)\)')

if __name__ == '__main__':
    with open('full_book.md', 'wt') as full_book_output:

        # find chapters and write out TOC
        chapters = []
        with open('README.md', 'rt') as main_input:
            for line in main_input:
                full_book_output.write(line)
                match = TOC_CHAPTER_PATTERN.match(line)
                if match:
                    chapters.append(match.groupdict()['path'])

        # append chapters in order
        for chapter in chapters:
            full_book_output.write('\n')
            with open(chapter, 'rt') as chapter_input:
                for line in chapter_input:
                    # fix any image links
                    match = IMAGE_LINK_PATTERN.match(line)
                    if match:
                        img = match.groupdict()
                        fixed_path = 'manuscript/' + img['path']
                        full_book_output.write('![{}]({})\n'.format(img['name'], fixed_path))
                    else:
                        full_book_output.write(line)
