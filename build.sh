#!/bin/bash
mkdir -p build
cd build
cmake .. && make -j

cd ..
cp ./build/replacesoh_impl.cpython-312-x86_64-linux-gnu.so ./kitetsu/

python setup.py sdist bdist_wheel

pip install ./dist/kitetsu-0.1-py3-none-any.whl

pip install build

python -m build

# vim ~/.pypirc
twine upload ./dist/kitetsu-0.1-py3-none-any.whl