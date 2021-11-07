Name:           psycopg
Version:        3.0.1
Release:        1%{?dist}
Summary:        New implementation of the most used, reliable and feature-rich PostgreSQL adapter for Python

License:        LGPLv3
URL:            https://github.com/psycopg/psycopg
Source0:        %{url}/archive/%{version}/psycopg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For check
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

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files psycopg

%check
%pytest

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sat Nov 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.0.1-1
- Initial package
