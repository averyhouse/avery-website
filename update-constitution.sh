#!/bin/bash
git submodule init
git submodule update --remote
pandoc constitution/constitution.md -o avery_website/templates/constitution-contents.html
