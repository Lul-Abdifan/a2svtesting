name: CI/CD Exercise

on:
  push:
    branches:
      - main

jobs:
  python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v3
        with:
          pythonversion: "3.x"
      - run: python --version