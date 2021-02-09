# srpa

Practice simple test automation with python.
[sample/](sample/) Folder contains examples that use [UNAPEC's](http://www.unapec.edu.do) website in json and yaml.

## Dependencies

- [python 3.8](https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe)
- [selenium](https://selenium-python.readthedocs.io/)
- [PyYaml](https://pypi.org/project/PyYAML/)
- Google, Firefox or any other webdriver [Google Chrome webdriver](https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_win32.zip)

## Install Dependencies

### Python 3.8

Just Download the python installer for your OS and install. In windows you might have to add the python installation dir to the PATH environment variable

### selenium

Once python 3.8 is installed then run:

```batch
python -m pip install -U selenium
```

### PyYAML

```batch
python -m pip install -U pyyaml
```

### Webdrivers

Download the webdriver (For this example just downloading the chrome webdriver will be OK) and put the executable in
an easy to find directory. These executables must be added to the PATH on windows.

## Package

You need to have pyinstaller installed.
If it's not installed install it with:

```batch
python -m pip install -U pyinstaller
```

Now just run the 'package.bat' script in windows or the 'package.sh' script for linux.
Or, for the same effect run:

```batch
python -m PyInstaller main.py --onefile -n srpa.exe
```

## Usage

```batch
srpa -i ./sample.json -b chrome
```

## CLI arguments

```text
    [ srpa ]

        -h, --help
            Muestra este texto de ayuda
        -i, --input
            Especifíca la ruta del archivo que contiene el script de automatización (requerido)
            Tipos de entrada soportados: ['json', 'yml']
        -b, --browser
            Indica cual navegador se desea utilizar (default chrome)
            Navegadores soportados: ['chrome', 'firefox', 'opera']
        -d --driver
            Indica cual librería se desea usar para manejar la automatización
            Drivers soportados: ['selenium']
        -p, --path
            Indica la ruta de los binarios de webdriver
            Por default se utilizan los encontrados en el PATH
```

## Script syntax

See the sample scripts in [sample/](sample/)