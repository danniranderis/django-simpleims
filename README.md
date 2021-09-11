# django-simpleims

This project is a simple inventory management system written in the [Django Web Framework](https://www.djangoproject.com/).

The goal is to provide a simple "turn-key" system that can be used to manage your inventory - be it warehousing, your Blu-ray collection or something else.


## Requirements
WIP.
 
## Usage
WIP.

## Dependencies
 - Python 3.9
 - Django 3.2
 - and more -- see Pipfile for the full list.


## Development
For development in this project, `pipenv` is used to facilitate project-dependencies and virtual environments.
So to develop on the project, ensure that Python and `pipenv` is installed in the correct versions.

### Setting up development environment
Follow these steps to set up the environment:

1. Download/clone repository.
2. Ensure Git, Python3, Pipenv is installed.
3. Create virtual environment and install dependencies via `pipenv install`.

### Pipenv commands
The following commands is useful for working with Pipenv -- see the full documentation on https://pipenv.pypa.io/en/latest/.

- `pipenv install` - Install/setup the venv from the definitions (if no pipfile is found in the current directory, then initialize a new).
- `pipenv install <package>` - Install a new/specific version of a package, and save to pipfile.
- `pipenv install 'django>=3.2.*'` - Ex. install Django in version 3.2-track, and save to pipfile.
- `pipenv shell` -  Start a shell within the virtual environment (use `exit` to exit out again).
- `pipenv update --outdated` - Get a list of outdated dependencies (used to see if updates is needed).
- `pipenv update` - Update all dependencies.
- `pipenv update <package>` - Update a specific dependency.
- `pipenv lock` - Create a new version of the `Pipfile.lock` from the `Pipfile`.
- `pipenv uninstall` - Uninstall all packages.
- `pipenv uninstall <package>` - Uninstall/remove package from dependencies.
- `pipenv uninstall --all` - Purge all files from the virtual environment, but don't touch the pipfile.
- `pipenv uninstall --all-dev` - Remove all development packages from the virtual environment, _and_ remove them from the pipfile.


### Making changes
Development of this repository is currently comprised of the following steps. 

1. Make changes to the code.
1. Test it using the `python manage.py runserver` from within the venv.
1. Run linting? WIP
1. Run django-tests? WIP
1. Iterate over the last 3 steps until the code is done.
1. Commit code to Git and push to GitHub.

## Deployment
WIP.


## License
MIT


## Author Information
This project is developed and maintained by [Danni Randeris](https://danniranderis.dk/), and is a private repository.