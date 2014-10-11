#make a pdf
build: clean
	mkdir build
	pdflatex -output-directory build writeup.tex
	cp build/writeup.tex .

#clean the build dir
clean:
	rm -rf build
