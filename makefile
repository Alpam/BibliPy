#compilsal -Wall -Wextra -Werror
#compilcov -fprogile-arcs -ftest-coverage

test:
	mkdir test
	python3 teste.py

clean:
	rm -r test
