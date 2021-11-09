Name:           psycopg
Version:        3.0.2
Release:        1%{?dist}
Summary:        New implementation of the most used, reliable and feature-rich PostgreSQL adapter for Python

License:        LGPLv3
URL:            https://github.com/psycopg/psycopg
Source0:        %{url}/archive/%{version}/psycopg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For check
BuildRequires:  pkgconfig(libpq)
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  pytest

%description
Google Drive API Python wrapper library. Maintained fork of PyDrive.

%package -n     python3-%{name}
Summary:        %{summary}

%description -n python3-%{name}
psycopg3 is the new implementation of the most used, reliable and feature-rich
PostgreSQL adapter for Python. psycopg3 design emerges from the experience of
more than 10 years of development and support of psycopg2. It embraces the new
possibilities offered by the more modern generations of the Python language and
the PostgreSQL database and addresses the challenges offered by the current
patterns in software development and deployment.

%prep
%autosetup -n psycopg-%{version}/psycopg
# works fine with latest pytest-asyncio
# https://github.com/psycopg/psycopg/pull/143
sed -i setup.py -e 's/"pytest-asyncio ~= 0.15.1",/"pytest-asyncio >= 0.15.1, <0.17.0",/'
# disable remove deps for typechecking and linting
sed -r -i 's/("(mypy|black|flake8|pytest-mypy)\b.*",)/# \1/' setup.py

# remove pproxy dep, only used in tests
sed -r -i 's/("(pproxy)\b.*",)/# \1/' setup.py

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files psycopg

%check
export PGTESTS_LOCALE=C.UTF-8
%postgresql_tests_run

export PSYCOPG_TEST_DSN="host=$PGHOST port=$PGPORT dbname=${PGTESTS_DATABASES##*:}"
cd ..
%pytest -k 'not test_typing and not test_version'

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Sat Nov 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.0.2-1
- Initial package
