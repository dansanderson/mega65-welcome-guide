make clean
make html
make singlehtml
make latexpdf
scp -r _build/html/* dsanders@dansanderson.com:/home/dsanders/dansanderson.com/mega65/welcome
scp -r _build/singlehtml/* dsanders@dansanderson.com:/home/dsanders/dansanderson.com/mega65/welcome/singlehtml
scp -r _build/latex/mega65welcomeguide.pdf dsanders@dansanderson.com:/home/dsanders/dansanderson.com/mega65/welcome/
