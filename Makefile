
install: install-pyctrl install-docs

.PHONY: install-pyctrl install-docs clean
install-pyctrl:
	git clone https://github.com/AB-QuantIC/dbbc3-py-mpifr.git
	cd dbbc3-py-mpifr/lib && sudo python setup.py install

install-docs:
	git clone https://github.com/AB-QuantIC/dbbc3-docs.git

clean:
	rm -rf dbbc3-py-mpifr
	rm -rf dbbc3-docs