TEST_FILES = $(shell find pystat/tests/ -type f \( -iname "*.py" ! -iname "__init__.py" \))

all:
	python setup.py build

test:
	for t in $(TEST_FILES) ; do \
		python $$t ; \
	done

coverage:
	for t in $(TEST_FILES) ; do \
		coverage run -a $$t ; \
	done

clean:
	rm -f $(shell find . -name '*.pyc' -type f)
	rm -f $(shell find . -name '.coverage' -type f)

install:
	python setup.py install
