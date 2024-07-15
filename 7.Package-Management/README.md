```
pip install setuptools twine
python setup.py sdist

conda create -n mycustompackage python=3.10
pip install dist/hello_world_akjshyfasa-0.0.1.tar.gz

twine upload --repository-url https://test.pypi.org/legacy/ \
  dist/hello_world_akjshyfasa-0.0.1.tar.gz

pip install -i https://test.pypi.org/simple/ hello-world-akjshyfasa==0.0.1

# Push the file to Prod server
twine upload --repository-url https://upload.pypi.org/legacy/ \
  dist/prediction_model_manifoldailearning-1.0.0.tar.gz

```