HOME=/home/scs/taylor/faculty/si486l/page

push: $(shell find -type f | grep '\.md' | sed 's/\.md/\.html/')
	rsync -avzr . web-ext01.erp.usna.edu:/www/webpages/nfsusers/Users/cs/taylor/courses/si486l/ --delete --exclude '*.md' --exclude '.*'

%.html: %.md
	pandoc -H $(HOME)/incCSS.html -B $(HOME)/topPart.html --highlight-style=zenburn $^ > $@

%.swp:
	echo test
