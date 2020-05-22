#!/usr/bin/env python3

# Copyright (c) 2020 Susam Pal
# Licensed under the terms of the MIT License.

# This software is a derivative of the original makesite.py available at
# <https://github.com/sunainapai/makesite>. The license text of the
# original makesite.py is included below.

# The MIT License (MIT)
#
# Copyright (c) 2018 Sunaina Pai
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import glob
import re
import os
import sys


def fread(filename):
    """Read file and close the file."""
    with open(filename, 'r') as f:
        return f.read()


def fwrite(filename, text):
    """Write content to file and close the file."""
    basedir = os.path.dirname(filename)
    if basedir != '' and not os.path.isdir(basedir):
        os.makedirs(basedir)
    with open(filename, 'w') as f:
        f.write(text)


def log(msg, *args):
    """Log message with specified arguments."""
    sys.stderr.write(msg.format(*args) + '\n')


def read_headers(text):
    """Parse headers in text and yield (key, value, end-index) tuples."""
    for match in re.finditer(r'\s*<!--\s*(.+?)\s*:\s*(.+?)\s*-->\s*|.+', text):
        if not match.group(1):
            break
        yield match.group(1), match.group(2), match.end()


def read_post(dirpath, filename):
    """Read content and metadata from file into a dictionary."""
    text = fread(os.path.join(dirpath, filename))
    end = 0
    content = {
        'id': os.path.basename(dirpath),
    }
    for key, val, end in read_headers(text):
        content[key] = val
    text = text[end:]
    processed = []
    for line in text.splitlines():
        if line.startswith('@include'):
            include_filename = line.split()[1]
            include_content = fread(os.path.join(dirpath, include_filename))
            processed.append(include_content.strip())
        else:
            processed.append(line)
    content['content'] = '\n'.join(processed)
    return content


def render(template, **params):
    """Replace placeholders in template with values from params."""
    return re.sub(r'{{\s*([^}\s]+)\s*}}',
                  lambda match: str(params.get(match.group(1), match.group(0))),
                  template)


def main():
    output = []
    readme_template = fread('src/readme-template.md')
    post_template = fread('src/post-template.md')

    items = []
    for dirpath in sorted(glob.glob('src/[0-9]*')):
        post = read_post(dirpath, 'post.md')
        item = render(post_template, **post)
        items.append(item)

    content = ''.join(items)
    output = render(readme_template, content=content)
    fwrite('README.md', output)


if __name__ == '__main__':
    main()
