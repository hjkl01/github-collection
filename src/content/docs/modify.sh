#!/bin/bash

for file in $(find /home/ljl/github/astro-project/src/content/docs -name "*.md" -type f); do
    if [[ "$file" == *"/dotfiles_hjkl01.md" ]]; then continue; fi  # skip the example
    basename=$(basename "$file" .md)
    # parse project and author
    author=$(echo "$basename" | rev | cut -d'_' -f1 | rev)
    project=$(echo "$basename" | sed "s/_$author$//")
    repo="$author/$project"
    # check if already has badge
    if grep -q "img.shields.io/github/stars" "$file"; then
        echo "Already has badge: $file"
        continue
    fi
    # add the line
    sed -i "5a\### [ ![GitHub Repo stars](https://img.shields.io/github/stars/$repo?style=social) ](https://github.com/$repo)" "$file"
    echo "Added to $file"
done