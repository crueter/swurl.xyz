#!/bin/bash
# This simply converts all HTML pages to GMI.
# This should be run from a directory that contains the full website in the
# "html" subdirectory, and "private" additionally symlinked
# into the gemini root directory.

for i in `find html -name "*.html"`
do
	declare to="`echo $i | cut -d'/' -f2-`"
	declare to="${to%.*}.gmi"
	private/html2gmi -i $i > $to
	sed -i 's/\.html/.gmi/g' $to
done
