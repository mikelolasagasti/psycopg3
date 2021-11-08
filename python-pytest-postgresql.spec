%global pypi_name pytest-postgresql
%global name_with_underscore pytest_postgresql

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        A pytest plugin for PostgreSQL database integration

License:        LGPLv3+
URL:            https://github.com/ClearcodeHQ/pytest-postgresql
Source0:        https://github.com/ClearcodeHQ/pytest-postgresql/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for check
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  python3-psycopg2
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-de

%description
This is a pytest plugin, that enables you to test your code that relies on a
running PostgreSQL Database. It allows you to specify fixtures for PostgreSQL
process and client.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This is a pytest plugin, that enables you to test your code that relies on a
running PostgreSQL Database. It allows you to specify fixtures for PostgreSQL
process and client.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name_with_underscore}

%check
%pytest --postgresql-exec="/usr/bin/pg_ctl" -k "not docker" --no-cov

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING COPYING.lesser
%doc AUTHORS.rst CHANGES.rst README.rst

%changelog
* Thu Oct 21 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.1.2-1
- Update to 3.1.2 #2016263

* Tue Aug 10 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.1.1-2
- Changes based on #1991138 review

* Fri Aug 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.1.1-1
- Initial version
